import argparse
import uuid
import json
import re
import urllib.request
import urllib.parse
from typing import List, Dict

# --- CONFIGURATION ---
COMFY_SERVER_ADDRESS = "127.0.0.1:8000"  # Target port 8000
CLIENT_ID = str(uuid.uuid4())

# Verified node tracking keys based on your exported layout format
PROMPT_NODE_ID = "105:104"    # MiniMax H3 Image to Video node
PROMPT_FIELD_KEY = "prompt"   # Input property key for text parameters

DURATION_NODE_ID = "105:111"  # Float (duration) Primitive node
DURATION_FIELD_KEY = "value"  # Input property key for numerical durations

def parse_markdown_shots(file_path: str) -> List[Dict[str, any]]:
    """Parses the markdown file to extract shot indices, cleaned prompts, and duration floats."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split the file by Markdown H2 headers (## Shot X)
    shot_blocks = re.split(r'(?=## Shot \d+)', content)
    parsed_batch = []

    for block in shot_blocks:
        if not block.strip() or not block.startswith("## Shot"):
            continue
            
        # Extract individual lines from the block safely
        lines = [line.strip() for line in block.split('\n') if line.strip()]
        if not lines:
            continue
        header_line = lines[0]
        
        # Regex to capture the Shot number, title text, and dynamic duration marker like (12s)
        title_match = re.match(r'^## Shot (\d+):\s*(.*?)(?:\s*\((?:~)?(\d+)s\))?$', header_line)
        if title_match:
            shot_number = int(title_match.group(1))
            shot_title_clean = title_match.group(2).strip()
            shot_duration = int(title_match.group(3)) if title_match.group(3) else 10
            shot_title = f"Shot {shot_number}: {shot_title_clean} ({shot_duration}s)"
        else:
            continue

        # Locate the Integrated Prose Description section
        prose_match = re.search(r'### Integrated Prose Description\s*\n(.*?)(\n###|\n---|\s*$)', block, re.DOTALL)
        if prose_match:
            prose_text = prose_match.group(1).strip()
            
            # Clean up internal timeline breakdown markers like [0s-4s], [4s-12s], etc.
            cleaned_prose = re.sub(r'\[\d+s-\d+(?:\.\d+)?s\]', '', prose_text)
            cleaned_prose = re.sub(r'\s+', ' ', cleaned_prose).strip()

            parsed_batch.append({
                "number": shot_number,
                "title": shot_title,
                "duration": shot_duration,
                "prompt": cleaned_prose
            })
            
    return parsed_batch

def queue_prompt(prompt_workflow: dict) -> str:
    """Enqueues the generated prompt JSON graph to the ComfyUI execution server."""
    p = {"prompt": prompt_workflow, "client_id": CLIENT_ID}
    data = json.dumps(p).encode('utf-8')
    req = urllib.request.Request(f"http://{COMFY_SERVER_ADDRESS}/prompt", data=data)
    response = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
    return response['prompt_id']

def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description="Batch process MiniMax H3 Markdown scenarios into ComfyUI.")
    parser.add_argument(
        "-s", "--shot", 
        type=int, 
        default=None, 
        help="Optional: Specify a single shot number to render (e.g., -s 5). If omitted, renders all shots."
    )
    args = parser.parse_args()

    # 1. Parse the workflow instructions text document
    md_file_path = "g_h3instr.md" 
    try:
        batch_tasks = parse_markdown_shots(md_file_path)
    except FileNotFoundError:
        print(f"[-] Error: Could not find '{md_file_path}' in the current working directory.")
        return

    # 2. Filter tasks if a specific single shot is requested via command line
    if args.shot is not None:
        batch_tasks = [task for task in batch_tasks if task["number"] == args.shot]
        if not batch_tasks:
            print(f"[-] Error: Shot number {args.shot} was not found inside the markdown file.")
            return
            
        print(f"[+] Targeted isolation mode: Processing ONLY Shot {args.shot}.")
    else:
        print(f"[+] Full batch mode: Processing all {len(batch_tasks)} shots found in file.")

    # 3. Load your exported ComfyUI API format workflow JSON graph
    try:
        with open("assets/workflows/video_minimax_h3_t2v_api.json", "r") as f:
            workflow_graph = json.load(f)
    except FileNotFoundError:
        print("[-] Error: 'video_minimax_h3_t2v.json' missing. Export it from ComfyUI Dev Mode first.")
        return

    # 4. Iterate and send the filtered tasks to the pipeline queue
    print(f"Starting execution of workflow task(s)...")
    for idx, task in enumerate(batch_tasks):
        # Inject parsed, cleaned prose prompt into the targeted ComfyUI text field
        workflow_graph[PROMPT_NODE_ID]["inputs"][PROMPT_FIELD_KEY] = task["prompt"]
        
        # Dynamically overwrite the duration value node
        if DURATION_NODE_ID in workflow_graph:
            workflow_graph[DURATION_NODE_ID]["inputs"][DURATION_FIELD_KEY] = task["duration"]
            duration_status = f"Duration set to: {task['duration']}s"
        else:
            duration_status = "Duration Node not found, using workspace default value"
        
        try:
            prompt_id = queue_prompt(workflow_graph)
            print(f"[Queue {idx+1}/{len(batch_tasks)}] Enqueued {task['title']}")
            print(f"   -> {duration_status}")
            print(f"   -> Comfy ID: {prompt_id}")
            print(f"   -> Prompt Snippet: {task['prompt'][:80]}...\n")
        except Exception as e:
            print(f"[-] Failed to enqueue {task['title']}: {e}\n")

    print("Targeted tasks successfully submitted to the ComfyUI backend queue.")

if __name__ == "__main__":
    main()

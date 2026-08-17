# Baba Yaga — AI Video Generation Project

A 3-minute animated film about Baba Yaga, the Slavic folklore witch. Built using **ComfyUI** with **MiniMax H3** video generation models, rendered locally on an AMD Ryzen 9 9900X (32 GB RAM) + RTX 5080.

The movie is constructed progressively across multiple acts, each act composed of individually rendered shots stitched together for continuity.

---

## Prerequisites

- **ComfyUI** — local video generation server
- **MiniMax H3** models — prompt-driven live-action cinematic video generation
- Hardware: AMD Ryzen 9 9900X · RTX 5080 · 32 GB RAM

## Project Structure

| File | Purpose |
|---|---|
| `storyboard.md` | Full screenplay, scene list, and shot-by-shot breakdown |
| `act_1.md` | Detailed screenplay for Act 1 — prose descriptions per shot |
| `h3instr_1.md` | MiniMax H3 prompt instructions for each shot in Act 1 |
| `g_h3instr.md` | General / global H3 writing guide and reusable patterns |
| `scene_summary.md` | Tabular summary of all scenes (scene, content, key shots) |
| `storyboard.pdf` | PDF export of the storyboard |
| `run_comfy_batch.py` | Python utility for parsing shot blocks from markdown and driving ComfyUI batch rendering |

## Workflow

1. Read the **MiniMax H3 prompt writing guide** to understand required sections per shot:

   https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_base_en.md

2. Review skills reference for agent-based prompt generation:
   https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills (locally: `h3-prompt-writing`)

3. Each shot follows this template — **all sections are required**:

   - Integrated Prose Description
   - Scene Background Description
   - Characters Description
   - Timeline Breakdown
   - Audio Layout
   - Style & Textures

4. Every shot is rendered independently by ComfyUI — there is no cross-shot memory. Each prompt must contain complete, repeated details to maintain visual continuity (characters, environment, lighting, style).

5. Shots are capped at **15 seconds** each per MiniMax H3 limits; longer moments are split.

## Act 1 Synopsis

Baba Yaga lives blissfully in her chicken-legged hut surrounded by a medieval garden. Four mischievous boys playing medieval football accidentally kick the ball into her house, breaking her lantern. Enraged, she deflates their ball — they curse her, banishing her to New York City. The next scene drops her medieval attire straight into a busy Port Authority Bus Terminal, where she eats a pigeon on camera and is surrounded by police. The act ends with her line in Russian: *"Sergey - local LLM's are not bad — embrace it!"*

## Notes

- Spoken dialogue is in English; character lines may include Russian
- Each scene/shot description must be **self-contained** so ComfyUI can render them independently without reference to prior shots
- Continuity between shots is maintained through repeated, complete descriptions rather than incremental edits — rewrite entire shot sections when modifying existing content

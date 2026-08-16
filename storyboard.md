# Baba Yaga Storyboard
- Create around 3 minute video movie with good audio about Baba Yaga
- It will be created using ComfyUI and MiniMax H3 models
- All this will be running on local machine - AMD Ryzen 9 9900X with 32GB RAM and GPU RTX 5080
- The movie will be progressively built. It will consists of multiple Acts.
- Use the minimax h3 prompt writing guide while generating the prompts:
    https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_base_en.md
- Agent skills: https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills, available locally as: h3-prompt-writing

## Goals
The following are the Goals:
a. To create screen play that will guide the video generation
b. To visualize the screen play using MiniMax H3 using comfyui tool 

## Screen play
### Synopsis:
This is story about about Baba Yaga - the Slavic folklore character

### Act-1
Act-1 is the introduction of Baba Yaga. Here is the summary of the scenes
1. Baba Yaga is blissfully living life in her hut sourrounded by beautiful medivial garden in deep woods - emphasis on blissfull living
2. The house is as described in folklore - in deep woods, hut standing on tall chicken legs - emphasis on chicken legs
3. There are mischivous boys (4) playing medivial football nearby
4. They accidentally kick the ball into Yaga's house breaking the lantern hanging in front of her house
5. Yaga coming running and seeing the wreckage, gets really mad and angry
6. She takes the ball and decides to teach the kids a lesson
7. The kids plead Yaga to give them the ball back
8. Yaga is in no mood to listen - she deflates the ball will her sharp finger nails - dramatic action of deflating
9. The ball busts into pieces
10. Seeing that, the kids gets really angry and curse Yaga - to be banished to New York City
11. Next scene should show the busy New York Port Authority Bus terminal
12. And suddenly Yaga appears in her medivial Slavic attaire in modern day busy Bus terminal
13. Suddenly people are in awe of this medivial woman from no where and staring at her
14. A pigon flies towards Yaga
15. Yaga grabs the pigon and eat it alive and gives a big burp - need to be dramatic
16. The people watching this action are really disgusted and starts murmors
17. Suddenly Port Authority Police arrive and sorround Yaga in dramatic fashion with dramatic music crescendo for finale of Act 1
18. In the final shot, Yaga say in Russian, "Sergey - local LLM's are not bad - embrace it!", with wicked smile
19. The spoken language by the characters in in English
20. End of Act-1

### Instructions
Use the Act-1 details labelled 1-20 above to do the following:
a. Create detailed scenes from the above description
b. For each scene build shots that will be used as prompts to MiniMax H3 workflow in ComfyUI
c. Note: the max length of any shot can only be 15 seconds - per MiniMax H3 - longer shots should be broken down
d. Each of these shots will be stiched together to form the full Act 1 video - so continutity between shots is important
e. Save the detailed screenplay for review as markdown file - named act_1.md
f. For each of the shots in act_1.md create detailed minimax-h3 instructions in file named h3instr_1.md
g. If you need to edit/change any shot section in act_1.md or h3instr_1.md, *rewrite/replace* the whole shot section instead of creating tools to edit/change specific lines/words
h. Each shot in h3instr_1.md *MUST* be detailed and follow all the MiniMax-H3 requirements and much have the following sections - Integrated Prose Description, Scene Background Description, Characters Description, Timeline Breakdown, Audio Layout, Style & Textures and any other relevant details - verify after you write each shot to double check it has all the sections mentioned - verify again each sections are written in each shot
i. Each shot *MUST* have proper timing that serves the emotional gravity of each moment
j. Each scene/shot will be rendered by the comfyui independently - it has no recollection of the prior scene's/shot's descriptions - so in each scene the details has to be complete (and repeated) - independent. this is *CRITICAL* to be consistent across scene/shots and maintain similarity and continuity of the scene and background
k. Summarize all the scenes in tablular format - example column headings: scene, content, key shots - named in file scene_summary.md
l. See an example how the shot has to be described:
--- shot description start
## Shot 2: Boys Playing Medieval Football (~15s)**
### Integrated Prose Description
Live-action, cinematic, medium-wide tracking shot from behind as four mischievous boys aged 8–12 dressed in tattered medieval tunics and leather boots run across the dirt garden path kicking an old worn-leather football with visible stitching. One boy wearing a pointed conical hat dribbles the ball past raised flowerbeds while another chases behind carrying a rough-hewn wooden shield strapped to his back. They laugh loudly, heads thrown back, as they sprint toward the garden perimeter fence, the leather ball bouncing rhythmically between their legs with each stride — thwack against stone, hop along dirt, thwack again — producing a lively staccato percussion that matches the energy of their movement and carries clearly through warm afternoon air.

### Scene Background Description
* **Mediavial forrest:** Rustic overgrown with medivial plants
* **Visual Profile:** Live-action, highly detailed cinematic realism, rich organic textures, sharp focus, naturalistic lighting with shallow depth of field.

### Characters Description
* **Character Profile <Yaga>:** Baba Yaga, an old Slavic folklore witch with deeply weathered, wrinkled skin, piercing dark eyes, sharp prominent cheekbones, and long, claw-like fingernails. She wears a rustic medieval Slavic outfit consisting of a tattered charcoal-grey wool tunic, a frayed burlap shawl pinned with a bone brooch, and a patterned crimson headscarf wrapping her silver hair.
* **Environment Profile <Hut>:** a rustic wooden log hut standing on two tall, scaly yellow chicken legs. The hut has a moss-covered thatch roof and a wooden front porch with a glowing glass lantern hanging from the overhanging eaves.

### Timeline Breakdown
[0s-2s] Tracking shot from behind at fast speed following boys running across packed earth path — leather boots thudding with each step kicking up small clouds of dust, conical hat bobbing above shoulders as oldest boy leads the pack dribbling ball between feet while younger ones flank him laughing breathlessly.
[2s-3.5s] Camera maintains medium-wide frame with moderate amplitude following their trajectory toward garden perimeter fence line — boys' medieval tunics flapping in warm breeze, one smaller boy trailing behind grinning as he watches the ball roll ahead of them while his companion yells encouragement and they all laugh together producing overlapping giggles that rise above ambient forest sounds.
[3.5s-4.5s] Ball arcs upward into frame as oldest boy lifts leg and kicks it high — camera tracks the flight arc at fast speed with small controlled amplitude keeping ball centered, leather panels catching golden afternoon light showing worn texture and stitching detail against blue sky background while boys' faces blur slightly in pursuit below.
[4.5s-6s] Hold on boys running ahead of flying ball with wind picking up from tree movement behind them — camera remains locked on group's backs as they continue sprinting toward fence line, laughter audible in background layering over rising whoosh of wind through birch branches producing natural atmospheric texture that builds anticipation for what lies just beyond garden boundary.

### Audio Layout
* **Diegetic soundscape:** Heavy tactical boots sprinting on concrete, the sharp metallic click of utility gear shifting, authoritative police shouting: <d>[en] "Step back! Don't move! Hands where I can see them!"</d>, and the deep, defiant animalistic growl from <Yaga>.
* **Non-diegetic orchestration:** A massive, driving orchestral crescendo featuring heavy war drums, screaming brass, and high-intensity percussion that rises to a deafening, dramatic peak before cutting instantly to black.

### Style & Textures
Realistic live-action cinematic, warm natural afternoon lighting catches boys' medieval costumes and leather boots showing texture detail — tattered tunics in faded earth tones catching golden light on edges while worn leather boots display scuffs and dirt marks from extensive play across garden paths. Slight motion blur on fast movement captures kinetic energy of running sequence without obscuring key details, shallow depth of field keeps garden background softly blurred into impressionistic bokeh circles formed by wildflowers catching sunlight behind running figures creating painterly backdrop that emphasizes boys' energetic foreground action throughout entire six-second duration from initial tracking through final hold moment.
--- shot description ends



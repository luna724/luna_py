> sd_tool / prompt_easymaker All Changelogs (v3β-1)

<details><br />+ Feature Addition <br />* Modify 
Already Feature <br />- Delete Feature <br/>= NO Update Upcoming</details>

## v3β-10 ~ Generation update [WIP]


\+ Define/Template: new args in ControlNet / ADetailer
\+ Define/Template: turn to loadable
\+ prompt keyword deletion in tiny tweaks
\+ prompt keybox Definition / Deletion / Restore / Sorting
\+ word Updater in tiny tweaks
\+ Delete/Template and Delete/LoRA are now working with new ui
\+ Define/Template: Selectable model in Hires upscaler, Sampling method, SD Model, ControlNet mode, ControlNet Model, ControlNet Preprocessor, ControlNet Control Mode, ADetailer Model! (some requires user definition)
\+ Character Exchanger is now working with new UI!
\+ Generate/Template: shown the selected character's extend prompt
\+ Generate/Template: accept more argument (INCOMPLETE).
\+ Sort is supported LoRA Template, Prompt Template, Keybox Template
\+ Define/Template: save template version are now selectable! (v3.0.3 / v3.0.6)
\* change webui build method (complete!)
\* Generate/Template: allow you to reload Character templates
\* v3.0.3 -> V3.0.6 Prompt Template

## v3β-9 ~ more readable and easy debugging webui
\+ add language system
\+ _2space, prompt keyword shuffle in tiny tweaks
\+ can Generate with Regional prompter's secondary prompt
\* Semi-realtime applicate in Generate/Template
\* custom LoRA(not defined lora) available in generation/template
\* change webui build method (incomplete)
\* Removed some old UI buttons
\* Extend prompt are now toggled! (Generate/Template)
\* Fix can't load example from prompt template
\* Fix missing commas in header and lower (Generate/Template)
\- removed some javascripts

## v3β-8 ~ a1111's style / character loras
\+ Prompt Template's Image path is turn to relpath from realpath (Experiment in Example Image)
\+ Restore Lora Template in WebUI (ONLY deleted by WebUI)
\+ Multiple restore Lora Template
\+ use javascript (copied from A1111/sd-webui)
\+ use CSS (copied from A1111/sd-webui)
\+ Prompt Template are now support Regional Prompter with multiple LoRA Template (maximum 2)
\+ Prompt Template can store lora weight for LoRA Character Template link
\+ Fix can't save duplicate image on Define / Prompt Template
\* change CustomNegative in Prompt Template WebUI Name (CustomNegative -> Memo)
\* Prompt Template Example system v3.0.3
\* Lora Character Database v4
\* append self key to Lora Charcater Database's value (v4) 
\* Character Exchanger can parsed multi character's LoRA (Experimental function / can toggle)
\* Character Exchanger's `Exchange Target` are now have a function
\* Character Exchanger - auto clipboard
\* Character Exchanger - Prompt Template Define Helper
\* script are accept argument from anywhere (launch.py or webui.py for launch ui)
\* new argument  "--local", "--loopui", "--ui_port \<port\>", "--open_browse", "--dev_restart", "--share", "--ui_ip"
\- Test mode webui

## v3β-7 ~ this is very capable WebUI?
\+ Restore Deleted Prompt Template (ONLY deleted by WebUI)
\+ Multiple Delete / Restore Prompt Template 
\+ Define Lora Template in WebUI
\+ Delete Lora Template in WebUI
\+ Multiple Delete Lora Template
\+ Template Generate are now Save all output Prompt
\+ Load Lora Template and input to Define tabs
\* Fix Prompt Template's Example System are not shown on Generate Tab [(#7)](https://github.com/luna724/luna_py/issues/7)
\* Catch "don't use character lora" Error [(#7)](https://github.com/luna724/luna_py/issues/7)
\* Database tab values can now be changed
\* [launch.py]'s new argument

## v3β-6 ~ Goodbye v1 Method and code
\* support ended for v1 feature / templates
\- Delete v1 / v2 Method support code
\- Moved v1 script to Archive

## v3β-5
\+ Prompt Template Delete in WebUI
\+ Prompt Template Example View in WebUI
\+ Prompt Template ControlNet View in WebUI 
\+ Prompt Template Version System
\+ Upcoming WebUI's config (β)
\* Prompt Template v3.0 -> v3.0.2
\* Prompt Template list are now displayed displayName

## v3β-4
v1 webui are now compatibility with gradio 3.41.2
Prompt Generate from Template System
Prompt Template Setup System
Database Tab
Prompt Character Lora Exchange system (with v3 lora character template system)
[Character Exchanger] now Save All inputted Prompt 
UPCOMING - A1111 SDWebUI Extension - SDTool Output Paster 

## v3β-3
Prereleased v3 Lora (character) template system
Lora (character) template updater

## v3β-2
build webui (for v3 (Template basic) Generation)
New Lora (character) template System
launch v1 option
used venv(lunapy) -> don't need localize install! (gradio and more..)

## v3β-1
create v3 method
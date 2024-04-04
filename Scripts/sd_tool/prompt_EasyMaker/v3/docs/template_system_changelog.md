> Template System Changelog

## v3.0.6 (ReleaseID: 6)
Image data save system changed. (imageRealPath -> imageRelPath)
rename ["Regional_Prompter"]["Secondary_Prompt"]["gFaL_from_main"] -> .["sync"]
delete some opts. <details> <summary> Deleted dict path </summary>
- /displayName
- /Database Path
</details>
add ["images"] for sharing template
add ["CFG"] for save CFG Scale

## v3.0.5 (ReleaseID: 5)
+6 generation variables

## v3.0.4 (ReleaseID: 4)
make_prompt_template.load() compatibility
rename ["Example"]["CustomNegative"] -> ["Example"]["Memo"]

## v3.0.3 (ReleaseID: 3)
Support Regional Prompter ( / Latent Couple) with maximum 2 LoRA<br />
can save Lora weight for Template LoRA System <br />

## v3.0.2 (ReleaseID: 2)
ControlNet / Hires.fix / Example) are auto toggle(if all value are blank, doesn't show on tab) for show status on Generate / Template Tab 
<details> <summary> All dict path </summary>
ConrtolNet: {key: {"ControlNet": {"isEnabled": bool}}} <br />
Hires.fix: {Key: {"Hires": {"isEnabled": bool}}} <br />
Example: {Key: {"Example": {"isEnabled": bool}}} <br />
</details> <br/>
Building the Foundation Code (No major code changes will be made in V3 in the future)
Release Template Prompt - Example View system

## v3.0.1 (ReleaseID: 1)
Method version is now support ReleaseID ({Key: { "Method_Release": int }}) </br>
Template LoRA System are compatibility with Template Prompt System ({ key: {"Example": {"Character": str}}})

## v3 (ReleaseID: {IndexError})
.
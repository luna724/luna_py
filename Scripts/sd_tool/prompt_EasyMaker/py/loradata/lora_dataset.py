# Syntax
# "view_target": ["Title", "Trigger Word", "LoRA Model Name", "Template", "sample_image_path_list", "image generation data"]
dataset = {
  "incoming hug": ["Incoming hug/kiss", ["incoming hug", "incoming kiss"], "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/3c2b90b5-82da-44b3-6844-979bc83f8600/width=760/287365.jpeg", r"""incoming hug, 1girl, solo, grey background, medium breasts, dress, Negative prompt: (worst quality, low quality:1.3), (depth of field, blurry:1.2), (greyscale, monochrome:1.1), 3D face, nose, cropped, lowres, text, jpeg artifacts, signature, watermark, username, blurry, artist name, trademark, watermark, title, multiple view, Reference sheet, EasyNegative, head out of frame, nsfw, Steps: 25, ENSD: 31337, Size: 512x576, Seed: 3969544621, Model: AbyssOrangeMix2_nsfw, Sampler: Euler a, CFG scale: 7, Clip skip: 2, Model hash: 0873291ac5, Hires resize: 760x920, AddNet Enabled: True, AddNet Model 1: incominghug(a140f2a4b73f), Hires upscaler: lollypop, AddNet Module 1: LoRA, AddNet Weight A 1: 1, AddNet Weight B 1: 1, Denoising strength: 0.35""", "https://civitai.com/models/21388/incoming-hugkiss"], 
  "incoming kiss": ["Incoming kiss",
  ["incoming kiss"], "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/e77337e0-99f5-4e1b-b2c0-725da19ba800/width=720/292104.jpeg", r"""1girl, solo, incoming kiss, dress, closed eyes,
Negative prompt: (worst quality, low quality:1.3), (depth of field, blurry:1.2), (greyscale, monochrome:1.1), 3D face, nose, cropped, lowres, text, jpeg artifacts, signature, watermark, username, blurry, artist name, trademark, watermark, title, multiple view, Reference sheet, EasyNegative, head out of frame, nsfw, bad-hands-5,
Steps: 25, ENSD: 31337, Size: 448x640, Seed: 1029003343, Model: AbyssOrangeMix2_nsfw, Sampler: Euler a, CFG scale: 7, Clip skip: 2, Model hash: 0873291ac5, Hires resize: 720x960, AddNet Enabled: True, AddNet Model 1: incoming_kiss(a586333fff9e), Hires upscaler: lollypop, AddNet Module 1: LoRA, AddNet Weight A 1: 1, AddNet Weight B 1: 1, Denoising strength: 0.3""", "https://civitai.com/models/22206/incoming-kiss"],
  "rei no himo": ["Rei no himo", ["rei no himo"],
  "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/e8ea2bf5-e8d8-4d6b-f70e-93d3c532b300/width=450/279044.jpeg", r"""1girl, solo, ((rei no himo)), white dress, ribbon, skindentation, medium breasts,
Negative prompt: (worst quality, low quality:1.3), (depth of field, blurry:1.2), (greyscale, monochrome:1.1), 3D face, nose, cropped, lowres, text, jpeg artifacts, signature, watermark, username, blurry, artist name, trademark, watermark, title, multiple view, Reference sheet, EasyNegative, head out of frame,
Steps: 25, Size: 448x640, Seed: 1914409639, Model: kotosmix_v10, Sampler: Euler a, CFG scale: 6, Clip skip: 2, Model hash: 49ef66fc4c, Hires resize: 720x960, AddNet Enabled: True, AddNet Model 1: rei_no_himoWD3_0(4a729073ea85), Hires upscaler: Latent, AddNet Module 1: LoRA, AddNet Weight A 1: 1, AddNet Weight B 1: 1, Denoising strength: 0.6""", "https://civitai.com/models/21066/rei-no-himo"],
  "in glass cup": ["girl in glass bottle", ["glass bottle", "glass cup"],
  "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/17b8785d-d3b8-4b84-91d2-82e561f0f700/width=450/154919.jpeg", "Can't Find Data", "https://civitai.com/models/13185/girl-in-glass-bottle"],
  "in box": ["Delivery In Box 宅配箱", ["in_box"],
             "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/4af0021a-86c0-476f-f0d1-75b767d6a900/width=450/25037-2723707952-masterpiece,solo,1girl,%20%20,in_box,blush.jpeg", r"""masterpiece,solo,1girl,  <lora:DeliveryV1-000006:1>,in_box,blush
Negative prompt: EasyNegative,bad-artist, bad hand,, ,bad_prompt_version2,sketch, duplicate, ugly, huge eyes, text, logo, monochrome, worst face, (bad and mutated hands:1.3), (worst quality:2.0), (low quality:2.0), (blurry:2.0), horror, geometry, bad_prompt, (bad hands), (missing fingers), multiple limbs, bad anatomy, (interlocked fingers:1.2), Ugly Fingers, (extra digit and hands and fingers and legs and arms:1.4), crown braid, ((2girl)), (deformed fingers:1.2), (long fingers:1.2), (bad-artist-anime),
Steps: 20, ENSD: 31337, Size: 400x600, Seed: 2723707952, Sampler: DPM++ 2M Karras, CFG scale: 7, Clip skip: 2, Model hash: a074b8864e, Hires steps: 10, Hires upscale: 1.8, Hires upscaler: ESRGAN_4x, Denoising strength: 0.5""", "https://civitai.com/models/9844/conceptdelivery-in-box"],
  "in water capsule": ["water_capsule", ["water_capsule"], 
                       "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/d381eb40-c085-4861-54b9-454d26ab9300/width=450/im_20230214234435_001_1589519578.jpeg", r"""Can't Find Data""", "https://civitai.com/models/9398/watercapsule"],
  "skin fang": ["Better Skin Fang - Concept", ["skin fang"],
                "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/41346a74-3fe2-4ae2-d4cd-f72a3bc48100/width=450/00065-3500680362.jpeg", r"""best quality, masterpiece, 1girl, black hair, short hair, red eyes, messy hair, skin fang, cowboy shot, :D
Negative prompt: (worst quality, low quality:1.4), (realistic, lip, nose, tooth, rouge, lipstick, eyeshadow:1.0), (dusty sunbeams:1.0), (abs, muscular, rib:1.0), (depth of field, bokeh, blurry:1.4), (greyscale, monochrome:1.0), text, title, logo, signature
Steps: 20, Size: 512x512, Seed: 3500680362, Model: anything-v4.5, Sampler: DPM++ SDE Karras, CFG scale: 7, Clip skip: 2, Model hash: 1d1e459f9f, Hires upscale: 2, AddNet Enabled: True, AddNet Model 1: skin_fang2(973d76ba62c3), Hires upscaler: Latent, AddNet Module 1: LoRA, AddNet Weight A 1: 0.6, AddNet Weight B 1: 0.6, Denoising strength: 0.6""", "https://civitai.com/models/11724/better-skin-fang-concept"],
  "cat eyes": ["Slit Pupils Inpaint - LoRA", ["slit pupils"],
               "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/1b3b02ea-39cb-42ac-da43-480afffa5f00/width=450/00037-4108486419.jpeg", r"""1girl, cat girl, looking at viewer, close-up face
Negative prompt: (nsfw:1.3), (worst quality, low quality:1.3), (depth of field, blurry:1.2), (greyscale, monochrome:1.1)
Steps: 20, ENSD: 31337, Size: 512x512, Seed: 4108486419, Model: AbyssOrangeMix2_sfw, Sampler: DPM++ 2M Karras, CFG scale: 7, Clip skip: 2, Model hash: 038ba203d8, Hires upscale: 2, Hires upscaler: Latent (nearest-exact), Denoising strength: 0.6""", "https://civitai.com/models/6346/slit-pupils-inpaint-lora"],
  "peace sign": ["LoRA Peace Sign✌", ["peace", "sign"],
                 "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/531fa338-8408-4450-b103-a2b94a3bce40/width=450/00017-132661117.jpeg", r"""peace, sign, smile, upper body portrait, anime, masterpiece, illustration, ultra-detailed, girl, 24yo women, nun sit on the bench at public garden, bench, shy, blushing, beautiful, beautiful face, beautiful eyes, detailed eyes, beautiful lips, green eyes, brown hair, short hair, volumetric shadow, volumetric lighting, green ribbon on the hair, green bow tie, green glasses, black outfit, tomboy, boyish, face focus, hand cuffs, crowd, long skirt
Negative prompt: EasyNegative, (worst quality:2), (low quality:2), (normal quality), lowres, (sketches), (monochrome), (grayscale), skin spots, acnes, skin blemishes, age spot, glans, extra fingers, strange finger, extra legs, strange leg, extra arms, strange arm, extra fingers, strange finger, extra limbs, strange limb, fat ass, hole, kid, naked, fat thigh, nsfw, nude, (leg open), (bad art, low detail, pencil drawing, old, oldest, mature:1.6), (plain background, grainy), (watermark, thin lines), (deformed, signature), (big nipples, ugly, bad anatomy, undersaturated, low resolution), bad proportions, poorly drawn face, poorly drawn hands, text, malformed, error, cropped, teeth, unsharp, breasts out, big breasts, nipples, wing, (lip, nose, tooth, rouge, lipstick, eyeshadow:1.4), (blush:1.2), (jpeg artifacts:1.4), (depth of field, bokeh, blurry, film grain, chromatic aberration, lens flare:1.0), (abs, muscular, rib:1.0), dusty sunbeams, trembling, motion lines, motion blur, emphasis lines, title, logo, white frame, freckles
Steps: 20, Size: 1280x1920, Seed: 132661117, Model: Counterfeit-V3.0_fp16, Sampler: DPM++ SDE Karras, CFG scale: 7, 'Overlap': 48, "{'Method': 'MultiDiffusion', 'Upscaler': 'R-ESRGAN 4x+ Anime6B', Model hash: cbfba64e66, 'Scale factor': 2, AddNet Enabled: True, AddNet Model 1: lora-dim8-peace-v0-3_sd-1-5(0a81bf082489), AddNet Module 1: LoRA, 'Keep input size': False}", 'Tile batch size': 1, AddNet Weight A 1: 0.9, AddNet Weight B 1: 0.9, Denoising strength: 0.2, 'Latent tile width': 96, 'Latent tile height': 96, Tiled Diffusion upscaler: R-ESRGAN 4x+ Anime6B, Tiled Diffusion scale factor: 2""", "https://civitai.com/models/48578/lora-peace-sign"],
  "ojousama pose": ["Ojou-Sama Pose (Concept LoRA)", ["ojou-sama pose"],
                    "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/5d93025f-4236-452a-b0c2-069ef504e700/width=1024/00072-2A_4116944768.jpeg", r""":3,
<lora:OjouSama:1>
1girl, ojou-sama pose, hand over own mouth, half-closed eyes, one arm behind back, witch, witch hat, dungeon, moss, cobblestone, contrast, dark lighting fantasy, torn clothes, white hair, purple eyes, short hair, bob cut, hair over one eye, single earring, single braid, detailed, masterpiece, graphite \(medium\), anime lineart, realistic
Negative prompt: (low quality, worst quality:1.4), (bad anatomy), (inaccurate limb:1.2), bad composition, inaccurate eyes, extra digit, fewer digits, (extra arms:1.2), closed eyes, (artist name, artist signature, signature:1.1)
Steps: 20, ENSD: 31337, Size: 512x768, Seed: 4116944768, Model: 2A, Sampler: DPM++ 2M Karras, CFG scale: 7, Clip skip: 2, Hires steps: 10, Hires upscale: 2, Hires upscaler: R-ESRGAN 4x+ Anime6B, Denoising strength: 0.55""", "https://civitai.com/models/51582/ojou-sama-pose-concept-lora"],
  "pov across table": ["pov across table concept", ["pov across table"],
                       "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/8ec2dc19-e234-4fd5-bb12-9043811b2e00/width=450/00268-804632829.jpeg", r"""1girl, pov across table, smile, table, outdoors, beach,
<lora:concept-pov_across_table-v1-000008:1>
Negative prompt: (worst quality, low quality:1.4),
Steps: 30, ENSD: 31337, Size: 512x768, Seed: 804632829, Model: AOM3, Sampler: Euler a, CFG scale: 5, Clip skip: 2, Model hash: d124fc18f0""", "https://civitai.com/models/46429?modelVersionId=51048"],
  "color": ["Colors", ["?"], "?", "None",
            r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/d1956261-7b62-4a9b-2770-d254983e1800/width=450/192212.jpeg", "", "https://civitai.com/models/15729?modelVersionId=18568"],
  "pocky game": ["Pocky Kiss Side View", ["\\<lora:pockyside1-000006:1\\>"],
                 "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/8a9a525b-5846-4a74-3579-260f5a7a8900/width=450/382069.jpeg", r"""<lora:pockySide1-000006:1>, 2girls, <lora:pekora1-000009:1>, pekora1, closed eyes, upper body, view from side, indoors, simple background, kissing, yuri
Negative prompt: EasyNegative, censored, multiple views, panels,
Steps: 28, ENSD: 31337, Size: 704x512, Seed: 3624459897, Model: AbyssOrangeMix2_hard, Sampler: DPM++ 2M Karras, CFG scale: 8, Clip skip: 2, Model hash: 0fc198c490""", "https://civitai.com/models/27960/pocky-kiss-side-view-or-test-concept-lora-231"],
  "yuri kiss": ["Yuri kiss", ["yuri", "kiss"],
                "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/068adcc7-23eb-4d96-8314-121ba7af9287/width=1024/00156-3177092060-30-8-DPM++%202M%20Karras-54ef3e3610.jpeg", r"""(masterpiece, best quality), 2girls, kissing, kiss, yuri, <lora:yurikiss:0.75>, standing, cherry blossoms background, sakura, windy, blush, embarrassed, <lora:add_detail:0.25> 
BREAK
Yae Miko, yaemikodef, <lora:yaemiko:0.75>
BREAK
Raiden Shogun, raidenshogundef, <lora:raidenshogun:0.75>
Negative prompt: easynegative, bad-hands-5
Steps: 30, Size: 512x768, Seed: 3177092060, Model: meinamix_meinaV11, Version: v1.4.1, Sampler: DPM++ 2M Karras, yaemiko: 3e68339f61cd, CFG scale: 8, Clip skip: 2, "yurikiss: 8bdbe4860bad, RP Active: True, RP Ratios: "1,1", Model hash: 54ef3e3610, add_detail: 7c6bad76eb54, Hires steps: 15, RP Use Base: True, RP Calc Mode: Attention, RP threshold: 0.4, raidenshogun: 8c2e28fdf17c", Hires upscale: 2, RP Change AND: False, RP Use Common: False, Hires upscaler: RealESRGAN_x4plus_anime_6B, RP Base Ratios: 0.5, RP Divide mode: Matrix, RP Use Ncommon: False, RP Mask submode: Mask, RP Matrix submode: Horizontal, RP Prompt submode: Prompt, Denoising strength: 0.4, RP LoRA Neg U Ratios: 0, RP LoRA Neg Te Ratios: 0""", "https://civitai.com/models/25152/yuri-kiss"],
  "yuri mutual masturbation": ["pose Mutual masturbation(yuri)", ["mutual masturbation"],
                               "WARN: This is LyCORIS Model", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/43f03816-149a-4d48-b14c-3a8bf23ab502/width=450/19448-1075076084-mutual%20masturbation,2girls,%20closed%20eyes,open%20mouth,blush,pussy%20juice,%20standing,looking%20at%20another,lying,spread%20legs,%20%20,%20masterpi.jpeg", r"""mutual masturbation,2girls, closed eyes,open mouth,blush,pussy juice, standing,looking at another,lying,spread legs,  <lora:Saya-mutual masturbation(yuri):1>, masterpiece,1girl,cute
Negative prompt: (worst quality:1.4), (low quality:1.4), (normal quality:1.4), lowres
Steps: 20, ENSD: 31337, Size: 640x896, Seed: 1075076084, Model: Anime_cetusMix_v4, Sampler: Euler a, CFG scale: 7, Clip skip: 2, Model hash: b42b09ff12, Hires steps: 15, Hires upscale: 1.5, Hires upscaler: R-ESRGAN 4x+ Anime6B, Denoising strength: 0.38""", "https://civitai.com/models/76001/pose-mutual-masturbationyuri"],
  "hoshi119's pov cunniling": ["POV yuri cunnilingus", ["cunnilingus", "female pov"],
                               "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/8ba5805e-1559-4ef5-aac9-941e104a5c00/width=450/00098-2243707821.jpeg", r"""masterpiece, best quality, 2girls, cunnilingus, female pov, <lora:qqq-cunnilingus_pov-v1:0.8>
Negative prompt: (worst quality, low quality:1.4), EasyNegative, bad anatomy, bad hands, cropped, missing fingers, missing toes, too many toes, too many fingers, missing arms, long neck, Humpbacked, deformed, disfigured, poorly drawn face, distorted face, mutation, mutated, extra limb, ugly, poorly drawn hands, missing limb, floating limbs, disconnected limbs, malformed hands, out of focus, long body, monochrome, symbol, text, logo, door frame, window frame, mirror frame
Steps: 20, Size: 512x512, Seed: 2243707821, Model: abyssorangemix2_Hard-003, Sampler: DPM++ SDE Karras, CFG scale: 7, Model hash: e714ee20aa""", "https://civitai.com/models/54539/pov-yuri-cunnilingus?modelVersionId=58906&prioritizedUserIds=837280&period=AllTime&sort=Most+Reactions&limit=20&active=true"],
  "69 yuri": ["69 Yuri", ["69", "yuri", "2girls"],
              "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/7c55a243-c2d7-4b78-a9d6-8f2f34da774e/width=450/00026-4179483105.jpeg", r"""(69), yuri, nude, side view, head between legs, (girl on top), cunnilingus, <lora:Yuri_69:0.8>
Negative prompt: multiple views, strangling, kiss, 3girls, (worst quality, low quality:2), lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, (signature:1.5), watermark, username, blurry, speech bubble, text, monochrome, censored, (low quality, worst quality, blurry) , ((panties)), pantsu , ((thongs)), ((underpants)), (many legs) (many hands), (((blue eyes)))
Steps: 20, Seed: 4179483105, Sampler: DPM++ SDE Karras, CFG scale: 7""", "https://civitai.com/models/100497/69-yuri"],
  "liquid clothes": ["Liquid Clothes", ["liquid clothes", "water"], "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/ed648018-21f4-4b36-872b-49fcb33b7cf1/width=1024/05755-4147613171-1girl,%20solo,%20((liquid%20clothes)),%20,_liquid%20clothes,%20blue%20theme,%201girl,%20solo,%20long%20hair,%20dress,%20barefoot,%20blue%20hair,%20one%20eye%20close.jpeg",
                    r"""1girl, solo, ((liquid clothes)), <lora:LiquidClothesV2:1>,
liquid clothes, blue theme, 1girl, solo, long hair, dress, barefoot, blue hair, one eye closed, blue eyes, blue nails, nail polish, toenail polish, cloud, toenails, full body, very long hair, sky print, blue dress, standing, sleeveless, looking at viewer, smile
Negative prompt: (worst quality, low quality:1.6), badhandsv4, monochrome, blurry, (nipples), pussy,
Steps: 20, ENSD: 31337, Size: 512x768, Seed: 4147613171, Model: SpiritForeseerMix-O, Sampler: DPM++ 2M Karras, CFG scale: 7, Clip skip: 2, Model hash: 1e0c69b67c, Hires steps: 10, Hires upscale: 2, Hires upscaler: ESRGAN_4x, Denoising strength: 0.5""", "https://civitai.com/models/71745/conceptliquid-clothesliquid-dress"],
  "bondage outfit/dominatrix": ["【Costume】Bondage Outfit/Dominatrix 拘束衣装",["bondage outfit", "harness", "o-ring"],
                                "?","None",r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/d5ac13b5-1bde-4dd4-86f3-8026649a5046/width=1024/01509-260059604-(flat%20color),%20black%20background,((flower)),%20flower_around_head,%20((spring%20_(season_))),_1girl,%20solo,%20large%20breasts,%20_white%20hair,%20v.jpeg", r"""(flat color), black background,((flower)), flower_around_head, ((spring \(season\))),
1girl, solo, large breasts, 
white hair, very long hair, 
<lora:BondageOutfitV2:1>,
bondage outfit, harness,  o-ring, cross pasties, no panties, crotch strap, groin,
((blossoms)),((colorful)),(best quality),
red eyes,  large breasts, collarbone, bare arms, ((arms behind back)),  
, metal collar, light smile, dappled sunlight, pointy ears,  metal_collar, chain, jewelry,
Negative prompt: (worst quality, low quality:1.6), badhandsv4, monochrome, blurry, ((female pubic hair)), nipples,((pussy)), (gloves:1.2)
Steps: 20, ENSD: 31337, Size: 512x704, Seed: 260059604, Model: PCQAfixed, Sampler: DPM++ 2M Karras, CFG scale: 7, Clip skip: 2, Model hash: 0d4e772d3b, Hires steps: 10, Hires upscale: 2, Hires upscaler: ESRGAN_4x, Denoising strength: 0.5""",
"https://civitai.com/models/19574/costumebondage-outfitdominatrix"],
  "miniskirt+": ["Microskirt", ["microskirt"], "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/63a27cf3-b8b8-4ff9-92db-6dc4b5df83fa/width=450/00128-2312879730.jpeg",
                 r"""<lora:microskirt_v0.2:1.0> 
1girl, microskirt, blonde hair, dancer,, masterpiece, best quality, highly detailed
Negative prompt: (worst quality, low quality:1.4)
Steps: 20, ENSD: 31337, Size: 512x768, Seed: 2312879730, Model: hassakuHentaiModel_v13, Version: v1.3.2, Sampler: Euler a, CFG scale: 7, Clip skip: 2, Model hash: 7eb674963a, Hires upscale: 2, Hires upscaler: 4x-UltraSharp, "microskirt_v0.2: 06871c7d0e26", Denoising strength: 0.3""",
"https://civitai.com/models/111458/microskirt"],
  "naked towel": ["Naked towel", ["naked towel"], "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/7f5e2275-caff-409a-86c5-b99060d24532/width=450/00262-3596099238.jpeg",
                  r"""<lora:naked_towel_v0.1:1>
1girl, naked towel, cowboy shot, wet, wet hair,, masterpiece, best quality, highly detailed
Negative prompt: navel, see-through,, (worst quality, low quality:1.4)
Steps: 20, ENSD: 31337, Size: 512x768, Seed: 3596099238, Model: hassakuHentaiModel_v13, Version: v1.3.2, Sampler: Euler a, CFG scale: 7, Clip skip: 2, Model hash: 7eb674963a, Hires upscale: 2, Hires upscaler: 4x_foolhardy_Remacri, "naked_towel_v0.1: e6abcf86ee9a", Denoising strength: 0.3"""],
  "clothes pull 446": ["Panty Pull / Clothes Pull | Clothing Lora 446", ["<lora:ppfs:1>"], "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/2031a3e6-298b-4bdd-c5cb-b4e16deccb00/width=450/36599-2856152948-,%20ump9%20(girls'%20frontline),%20girls'%20frontline,%20monster%20energy,%20tianliang%20duohe%20fangdongye,%201girl,%20aged%20down,%20assisted%20exposure,%20bl.jpeg", r"""No Data""",
                       "https://civitai.com/models/8406/panty-pull-clothes-pull-or-clothing-lora-446"],
  "track uniform": ["Track Uniform (陸上競技)", ["rikujou", "track and field", "track uniforms", "sportswear", "sports bras", "sports bikinis"], "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/b8773e49-7cf0-4b02-50d0-c394f6dfcb00/width=450/340321.jpeg0", r"""1girl, rikujou, multiple girls, (masterpiece, high quality), mature female,group picture
Negative prompt: EasyNegative, (worst quality, low quality:1.2), signature, watermark, username,(loli:1.5)
Steps: 20, ENSD: 31337, Size: 512x704, Seed: 2884579992, Model: meinapastel_V4, Sampler: DPM++ 2M Karras, CFG scale: 7, Clip skip: 2, Model hash: 771c8fd970, Hires upscale: 2, AddNet Enabled: True, AddNet Model 1: TrackUniform_v1JP(91e76bec4ca1), Hires upscaler: SwinIR_4x, AddNet Module 1: LoRA, AddNet Weight A 1: 1, AddNet Weight B 1: 1, Denoising strength: 0.3""",
"https://civitai.com/models/25081?modelVersionId=30001"],
  "greek cloth": ["【Costume】Greek Clothes ギリシャ風服装", ["greek clothes", "peplos"], "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/01cf1ab4-9ec4-4d0c-acc7-92a501aa23b4/width=450/56098-864406886-1girl,solo,,%20greek%20clothes,%20peplos,%20laurel%20crown,%20armlet,%20%20,_sitting,outdoors,lake,rock,reeds,%20white%20hair,%20long%20hair,%20golden%20app.jpeg", r"""1girl,solo,, greek clothes, peplos, laurel crown, armlet,  <lora:GreekClothes:1>,
sitting,outdoors,lake,rock,reeds, white hair, long hair, golden apple, see-through,
Negative prompt: EasyNegative,(worst quality:1.4), (low quality:1.4), (normal quality:1.4), ((female pubic hair:1.3)), lowres,
Steps: 20, ENSD: 31337, Size: 512x640, Seed: 864406886, Sampler: DPM++ 2M Karras, CFG scale: 7, Clip skip: 2, Model hash: e7cfbb1120, Hires steps: 10, Hires upscale: 2, Hires upscaler: ESRGAN_4x, Denoising strength: 0.55""",
"https://civitai.com/models/80023/costumegreek-clothes"],
  "plastic bag": ["plastic bag　ビニール袋", ["plastic bag,swimsuit,"], "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/c8e050ed-99d8-41db-93d5-0c12de8a69e6/width=450/00016-902504340.jpeg", r"""nsfw,(masterpiece, top quality, best quality, official art, beautiful and aesthetic:1.2), (1girl,cute,short body:1.5), extreme detailed, colorful, highest detailed, ((ultra-detailed)), (highly detailed CG illustration), ((an extremely delicate and beautiful)),(ultimate shiny skin, ultimate detailed skin, ultimate detailed face),(outdoors, ocean, black hair, super long twintails, standing, blue eyes, narrow waist, large breasts, ribbon choker, light particles, lens flare, depth of field, sparkle, bokeh, dappled sunlight, day, plastic bag,swimsuit, hands on breasts, see-through:1.4), pussy, pussy juice stain, pussy juice trail, smile (solo focus, looking at viewer:1.5),<lora:flat2:-1.5>, <lora:plastic bag:1>
Negative prompt: EasyNegative, longbody, lowres, bad anatomy, bad hands, missing fingers, pubic hair, extra digit, fewer digits, cropped, worst quality, low quality, negative_hand-neg,<lora:flat2:1>, ng_deepnegative_v1_75t
Steps: 20, Size: 1024x1536, Seed: 902504340, Model: LimeREmix_sweet, Sampler: Euler a, CFG scale: 7, Clip skip: 2, Mask blur: 4, "{'Method': 'MultiDiffusion', 'Upscaler': 'R-ESRGAN 4x+ Anime6B', Model hash: 319d79821d, 'Tile Overlap': 48, 'Upscale factor': 1, 'Keep input size': True}", 'Tile batch size': 1, 'Tile tile width': 96, 'Tile tile height': 96, Denoising strength: 0.3, Tiled Diffusion upscaler: R-ESRGAN 4x+ Anime6B, Tiled Diffusion scale factor: 1""",
"https://civitai.com/models/26266/plastic-bag"],
  "better naked bathrobe": ["【Costume】Better Naked Bathrobe より良い裸バスローブ", ["naked bathrobe"], "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/f3b79591-c5e6-4059-a6e6-1d67d5636f8c/width=450/51352-3624547692-naked%20bathrobe,%201girl,%20minami%20kotori,%20breasts,%20solo,%20long%20hair,%20looking%20at%20viewer,%20bangs,%20large%20breasts,%20long%20sleeves,%20hair%20bow,.jpeg", r"""naked bathrobe, 1girl, minami kotori, breasts, solo, long hair, looking at viewer, bangs, large breasts, long sleeves, hair bow, indoors, one side up, bow, closed mouth, smile, brown hair, cowboy shot, brown eyes, green bow, yellow eyes, single hair ring, collarbone, blunt bangs, standing, cleavage, <lora:NakedBathrobeV1:1>
Negative prompt: EasyNegative,(worst quality:1.4), (low quality:1.4), (normal quality:1.4), ((female pubic hair:1.3)), lowres,penis,jacket,nipples,
Steps: 20, ENSD: 31337, Size: 512x640, Seed: 3624547692, Sampler: DPM++ 2M Karras, CFG scale: 7, Clip skip: 2, Model hash: 6bdb906885, Hires steps: 10, Hires upscale: 2, Hires upscaler: ESRGAN_4x, Denoising strength: 0.56""",
"https://civitai.com/models/58670/costumebetter-naked-bathrobe"],
  "morrigan aensland (vampire)": ["【Costume】【Cosplay】Morrigan Aensland (Vampire) Clothing", ["highleg leotard", "print pantyhose", "bat print", "head wings", "bat wings", "bridal gauntlets"], "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/5e14a601-7f8b-4390-839b-40ce8736ea55/width=450/9.jpeg", r"""
Steps: 35, Size: 768x512, Seed: 3205038627, Model: control_v11p_sd15_openpose [cab727d4], Weight: 1, "Module: none, Version: v1.5.2, Sampler: DPM++ 2M Karras, Low Vram: False, CFG scale: 7, Clip skip: 2, Model hash: 7400fefd36, Hires steps: 14, Resize Mode: Crop and Resize, Threshold A: 64, Threshold B: 64, Control Mode: Balanced", Guidance End: 1, "easynegative: c74b4e810b03", Hires upscale: 2.2, Pixel Perfect: False, Processor Res: 512, AddNet Enabled: True, AddNet Model 1: MorriganHighLeotardPrintPantyhoseBatPrint(78cf9e865520), Guidance Start: 0, Hires upscaler: BSRGAN, AddNet Module 1: LoRA, AddNet Weight A 1: 1, AddNet Weight B 1: 1, Denoising strength: 0.55""",
"https://civitai.com/models/128213/costumecosplaymorrigan-aensland-vampire-clothing"],
  "dangerous beast cosplay": ["【Costume】Dangerous Beast Cosplay 危険な獣Cos", ["dangerousbeast", "elbow gloves", "gloves", "wolf tail"], "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/c6eb4605-7890-4666-a0cf-fbb94e4e98d7/width=450/50785-505050141-1girl,%20dangerousbeast,solo,large%20breasts,wolf%20tail,%20elbow%20gloves,%20gloves,,wariza,%20fake%20animal%20ears,%20full%20body,.jpeg", r"""1girl, dangerousbeast,solo,large breasts,wolf tail, elbow gloves, gloves,<lora:DangerousBeastV2:1>,wariza, fake animal ears, full body,
Negative prompt: EasyNegative,(worst quality:1.4), (low quality:1.4), (normal quality:1.4), ((female pubic hair:1.3)), lowres,penis,
Steps: 20, ENSD: 31337, Size: 512x640, Seed: 505050141, Sampler: DPM++ 2M Karras, CFG scale: 7, Clip skip: 2, Model hash: f75b19923f, Hires steps: 10, Hires upscale: 2, Hires upscaler: ESRGAN_4x, Denoising strength: 0.56""",
"https://civitai.com/models/10429?modelVersionId=61470"],
  "onesie pajamas": ["Onesie Pajamas", ["anesie", "onesie"], "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/4575981a-ac28-4813-a0ce-9c36dc22076d/width=450/Onesies%20Date.jpeg", r"""onesie, POV, blush, smile, looking at viewer, sleepy, half-closed eyes,
Negative prompt: (worst quality, low quality, large head, extra digits:1.4), easynegative,
Steps: 23, Seed: 1234567890, Sampler: Euler a, CFG scale: 5""", "https://civitai.com/models/134866?modelVersionId=156026"],
  "highleg sideless leotard": ["【Costume】Highleg Sideless Leotard & Sideless Outfit", ["leotard", "black leotard", "blue leotard"], "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/bedebad0-54af-4566-a877-df44df580b4f/transcode=true,width=450/sideless.mp4", r"""1girl,solo,medium breasts,red eyes, 
wedding dress,bare legs, bare arms, 
 <lora:SidelessLeotard:1>,
standing, seaside,blue sky, no_panties,sideless,facing viewer, white hair, long hair,
Negative prompt: EasyNegative,(worst quality:1.4), (low quality:1.4), (normal quality:1.4), ((female pubic hair:1.3)), lowres,badhandsv4,open clothes,detached sleeves, jacket, twintails,
Steps: 20, ENSD: 31337, Size: 512x640, Seed: 2116465321, Model: DonutHoleMix-Beta, Sampler: DPM++ 2M Karras, CFG scale: 7, Clip skip: 2, Model hash: e7cfbb1120, Hires steps: 10, Hires upscale: 2, Hires upscaler: ESRGAN_4x, Denoising strength: 0.5""",
"https://civitai.com/models/110899/costumehighleg-sideless-leotard-and-sideless-outfit-and"],
  "cheerleader (bluearchive)": ["Cheerleader Outfit Blue Archive", [r"pom pom \(cheerleading\)", "holding pom poms", "miniskirt", "skirt", "crop top", "cheerleader"], "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/0cda7c6d-e228-41cc-452b-b6ac0b0cb900/width=450/291650.jpeg", r"""masterpiece, best quality, ultra-detailed, illustration, 1girl, shiroko, grey hair, blue eyes, animal ears, medium breasts, cheerleader, crop top, miniskirt, bare shoulders, skirt, standing, halo, holding pom poms, pom pom \(cheerleading\),  <lora:sunaookamiShirokoV1:0.5>,  <lora:cheerleaderOutfitV2:1>
Negative prompt: (worst quality, low quality:1.4), (realistic, lip, nose, tooth, rouge, lipstick, eyeshadow:1.0), (dusty sunbeams:1.0),(abs, muscular, rib:1.0), (depth of field, bokeh, blurry:1.4), (greyscale, monochrome:1.0), text, title, logo, signature,
Steps: 30, Size: 512x768, Seed: 1114736198, Model: meinahentai_v2, Sampler: DPM++ 2M Karras, CFG scale: 7, Clip skip: 2, Model hash: e7640356f8, Hires upscale: 2, Hires upscaler: 4x-AnimeSharp, Denoising strength: 0.5""",
"https://civitai.com/models/22162/cheerleader-outfit-blue-archive"],
  "whb (by. sevora)": ["wooden horse", ["nsfw", "pussy", "bound", "bondage", "bdsm", "woodenhor"], "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/65b4eef8-5738-4784-808f-a222d35aae98/width=450/193639-2825920727-nsfw,%20pussy,%20(solo,%201girl)%20(digital)%20(%20in%20detailed%20basement,%20%20(bound,%20bondage,%20bdsm))%20,%20best%20quality,%20%20%20%20woodenhor,.jpeg", r"""nsfw, pussy, (solo, 1girl) (digital) ( in detailed basement,  (bound, bondage, bdsm)) , best quality, <lora:boldline:0.2>  <lora:hairdetailer:0.2> woodenhor, <lora:woodenhor:1>
Negative prompt: (worst quality, low quality:1.4) bad-artist bad-hands-5 bad-image-v2-39000 badhandv4 verybadimagenegative_v1.3 EasyNegative, 3d
Steps: 30, ENSD: 31337, Size: 512x720, Seed: 2825920727, Model: sakushimixHentai_sakushiV20, Version: v1.4.1, Sampler: Euler a, CFG scale: 6.5, Clip skip: 2, "boldline: d6fd61680d05, woodenhor: e3b7dbaa20d4", Model hash: c5328cf102, hairdetailer: 528c2e4d0627, Hires upscale: 2, Hires upscaler: 4x-UltraSharp, ADetailer model: face_yolov8n.pt, ADetailer version: 23.7.5, Denoising strength: 0.4, ADetailer mask blur: 4, ADetailer confidence: 0.3, ADetailer dilate/erode: 4, ADetailer inpaint padding: 32, ADetailer denoising strength: 0.4, ADetailer inpaint only masked: True""",
"https://civitai.com/models/109655?modelVersionId=118166"],
  "hospital gown": ["A Certain Kind of Hospital Gown 病院のガウン", ["hospital gown"], "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/3224bd2b-b471-447a-a694-d1a3df9986be/width=450/53040-1839771434-hospital%20gown,%201girl,%20long%20hair,%20solo,%20hair%20between%20eyes,%20very%20long%20hair,%20indoors,%20bangs,%20sitting,%20collarbone,%20shiny%20hair,%20red%20e.jpeg", r"""hospital gown, 1girl, long hair, solo, hair between eyes, very long hair, indoors, bangs, sitting, collarbone, shiny hair, red eyes, bedroom, shiny, pillow, short sleeves, hospital bed, bed, white hair, open mouth, sunlight, parted lips,  <lora:HospitalGownAV1:1>,
Negative prompt: EasyNegative,(worst quality:1.4), (low quality:1.4), (normal quality:1.4), ((female pubic hair:1.3)), lowres,
Steps: 20, ENSD: 31337, Size: 512x640, Seed: 1839771434, Sampler: DPM++ 2M Karras, CFG scale: 7, Clip skip: 2, Model hash: f75b19923f, Hires steps: 10, Hires upscale: 2, Hires upscaler: ESRGAN_4x, Denoising strength: 0.56""", "https://civitai.com/models/68475/a-certain-kind-of-hospital-gown"],
  "whb (by. psoft)": ["Wooden horse / bdsm", ["wooden horse", "crotch rub"], "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/76ba2545-3463-432f-b661-934077997766/width=450/04074-1757019989.jpeg", r"""<lora:wooden_horse_v0.2:1>
1girl, crotch rub, wooden horse, dress, frills, holding plate, food, eating,, masterpiece, best quality, highly detailed
Negative prompt: (worst quality, low quality:1.4)
Steps: 20, ENSD: 31337, Size: 512x768, Seed: 1757019989, Model: hassakuHentaiModel_v13, Version: v1.3.2, Sampler: Euler a, CFG scale: 7, Clip skip: 2, Model hash: 7eb674963a, Hires upscale: 2, Hires upscaler: 4x-UltraSharp, "wooden_horse_v0.2: d27a1ace4f5c", Denoising strength: 0.2""","https://civitai.com/models/116918/wooden-horse-bdsm"],
  "akuma homura's blackdress": ["【Costume】【Cosplay】Akuma Homura's Black Dress", ["black dress", "argyle legwear"], "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/41e5ee5f-5bc6-4698-a480-9892d3116293/width=450/64205-1618519041-black%20dress,%201girl,%20solo,%20long%20hair,%20black%20hair,%20purple%20eyes,%20gloves,%20elbow%20gloves,%20argyle%20legwear,%20smile,%20wings,%20argyle,%20bow,%20h.jpeg", r"""black dress, 1girl, solo, long hair, black hair, purple eyes, gloves, elbow gloves, argyle legwear, smile, wings, argyle, bow, hair bow, black gloves, breasts, looking at viewer, simple background, cleavage, large breasts, feathered wings, black wings,sweat,blush,hetero, embarrassed, wince,
 <lora:AkumaHomuraBlackDress:1>,
Negative prompt: EasyNegative, (worst quality:1.4), (low quality:1.4), (normal quality:1.4), ((female pubic hair:1.3)), lowres,bad anatomy, badhandsv4,
Steps: 20, ENSD: 31337, Size: 512x640, Seed: 3315220514, Model: AbyssalRavenMix-T, Sampler: DPM++ 2M Karras, CFG scale: 7, Clip skip: 2, Model hash: 46f562b139, Hires steps: 10, Hires upscale: 2, Hires upscaler: ESRGAN_4x, Denoising strength: 0.5""", "https://civitai.com/models/104957/costumecosplayakuma-homuras-black-dress"],
  "bondage amine": ["Bondage_Amine", ["bdsm,bondage, rope，shibari", "bdsm", "bondage", "rope", "shibari"], "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/ad47dcb7-f2a3-49b4-bdea-e521ec1bc64b/width=450/00886-183905454-masterpiece,high%20quality%20,%208k,1girl,%20solo,%20down,%20rope,%201girl,%20bound%20arms,%20%20legs%20bondage,rope%20bondage,bdsm,%20shibari,in1,%20side%20pon.jpeg", r"""1girl, solo, suspension, down, rope, 1girl, bodysuit, bound arms, indoors, leotard, bdsm, shibari, arms behind back, restrained, navel, leaning forward, feet,

Negative prompt: easynegative， negative_hand-neg，lowres, bad anatomy, bad hands, text, error, missing fingers, bad face，extra digit, fewer digits, cropped, worst quality, low quality, normal quality, artifacts, signature, watermark, username, blurry, missing arms, long neck, humpbacked, bad feet, nsfw ，malformed limbs, more than 2 thighs, extra legs, poorly drawn hands,band mouse""", "https://civitai.com/models/69589/bondageamine?modelVersionId=74253"],
  "masusu breasts": ["masusu_BreastAndNipples", ["不明"], "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/e880b91c-e53f-46be-988d-ad51385407bd/width=2880/00129-492675892.jpeg", r"""masterpiece, best quality, sidelighting,
3d face, realistic, lustrous skin,
1girl, kneeling, leaning forward, outdoors,
silver hair, side ponytail, long hair, green eyes, (sad, crying, teardrop, angry, scowl, glaring, full blush:1.2), clenched teeth,
large breasts, nipples, long nipples, puffy nipples, small areolae,
sweat, steam, steaming body, heavy breathing, arms behind back,
bdsm, rope, shibari, bondage, <lora:BondageAmine:0>,
mlik, lactation, milking machine, <lora:MilkingMachineV14:0>,
cape, topless, nahidadef, <lora:nahida1_000010:0.75>,
Negative prompt: EasyNegative,
Steps: 20, ENSD: 31337, Size: 2880x3840, Seed: 492675892, Model: facebombmix_v1Bakedvae, Version: v1.4.1, Sampler: Euler a, CFG scale: 7, Clip skip: 2, Model hash: 7364c31aac, "BondageAmine: 8468a6c04808, nahida1_000010: 7f892ec03340", MilkingMachineV14: 566281f45918, Denoising strength: 0.1""","https://civit.ai"],
  "standing cunnillingus": ["concept Standing cunnilingus", ["standing cunnilingus"], "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/d018a13d-8298-4c46-b920-f61e4e243700/width=450/127035-94802694-2girls,yuri,standing%20cunnilingus,white%20dress,clothes%20lift,ahegao,nose%20blush,%20panties%20around%20one%20leg,.jpeg", r"""2girls,yuri,standing cunnilingus,white dress,clothes lift,ahegao,nose blush, panties around one leg,
Negative prompt: (worst quality:1.4), (low quality:1.4), (normal quality:1.4), lowres
Steps: 20, ENSD: 31337, Size: 640x896, Seed: 94802694, Sampler: DPM++ 2M Karras, CFG scale: 7, Clip skip: 2, Model hash: e911995387, Hires steps: 12, Hires upscale: 1.5, AddNet Enabled: True, AddNet Model 1: standing cunnilingus-000010(d174eac5a433), Hires upscaler: R-ESRGAN 4x+ Anime6B, AddNet Module 1: LoRA, AddNet Weight A 1: 1, AddNet Weight B 1: 1, Denoising strength: 0.35""",
"https://civitai.com/models/55879/concept-standing-cunnilingus?modelVersionId=60276"],
  "milking machine": ["Milking machine", ["milking machine"], "?", "None", r"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/d05cdc1a-df28-4e32-ba3d-5365a48cc51b/width=450/tmpsd6257ea.jpeg", r"""milking machine, 1girl, solo, nipples, medium breasts, lactation, long hair, cow print, thighhighs, black bodysuit, leaning forward, elbow gloves, indoors, panties, window, arms up, cow ears, cow horns,
Negative prompt: (EasyNegative:1.0), negative_hand-neg,
Steps: 30, Size: 420x520, Seed: 2712218647, Model: AbyssOrangeMix2_nsfw, Version: v1.3.2, Sampler: DPM++ 2M Karras, CFG scale: 7, Clip skip: 2, Model hash: 0873291ac5, Hires steps: 25, Hires upscale: 1.7, AddNet Enabled: True, AddNet Model 1: milking_machineLoCon(bff1fdb3b9d8), Hires upscaler: 4x_fatal_Anime_500000_G, AddNet Module 1: LoRA, AddNet Weight A 1: 1, AddNet Weight B 1: 1, Denoising strength: 0.4""",
"https://civitai.com/models/8500?modelVersionId=112103"],
  "": []
}


def html(lora):
  cd = "D:/data/Dataset/Stable-Diffusion/Prompt/EasyMaker/py"
  
  # まず摘出
  data = dataset[lora]
  
  TITLE = data[0]
  TRIGGER_WORD = data[1]
  LORA_NAME = data[2].replace("<", "\\<").replace(">", "\\>")
  TEMPLATE = data[3].replace("<", "\\<").replace(">", "\\>")
  SAMPLE_IMAGE_PATH = data[4]
  SAMPLE_IMAGE_DATA = data[5].replace("\n", "   ")
  URL = data[6]
  
  viewed_markdown = f"""
  # {TITLE} 
  | Trigger Word | {TRIGGER_WORD} |
  | --- | --- |
  | LoRA Prompt Name | {LORA_NAME} |
  | Prompt Example | <details> <summary> Click to Open</summary> {TEMPLATE} </details> |
  | Sample Image | <details> <summary> Click to Open </summary> <img src="{SAMPLE_IMAGE_PATH}"> </details> |
  | Sample Image Generation Data | <details> <summary> Click to Open </summary> {SAMPLE_IMAGE_DATA} </details> |
  | View CivitAI (URL) | {URL} |
"""
  civitai_html = r"""<details> <summary> CivitAI HTML Preview </summary> Traceback (most recent call last):
  File "E:\Application\python\python3109\lib\site-packages\gradio\routes.py", line 442, in run_predict
    output = await app.get_blocks().process_api(
  File "E:\Application\python\python3109\lib\site-packages\gradio\blocks.py", line 1389, in process_api
    result = await self.call_function(
  File "E:\Application\python\python3109\lib\site-packages\gradio\blocks.py", line 1094, in call_function
    prediction = await anyio.to_thread.run_sync(
  File "E:\Application\python\python3109\lib\site-packages\anyio\to_thread.py", line 33, in run_sync
    return await get_asynclib().run_sync_in_worker_thread(
  File "E:\Application\python\python3109\lib\site-packages\anyio\_backends\_asyncio.py", line 877, in run_sync_in_worker_thread
    return await future
  File "E:\Application\python\python3109\lib\site-packages\anyio\_backends\_asyncio.py", line 807, in run
    result = context.run(func, *args)
  File "E:\Application\python\python3109\lib\site-packages\gradio\utils.py", line 703, in wrapper
    response = f(*args, **kwargs)
  File "D:\data\Dataset\Stable-Diffusion\Prompt\EasyMaker\py\lora_info_viewer.py", line 50, in main
    info, html = data.html(view_target.lower())
  File "D:\data\Dataset\Stable-Diffusion\Prompt\EasyMaker\py\loradata\lora_dataset.py", line 31, in html
    civitai_html = f.read()
  UnicodeDecodeError: 'cp932' codec can't decode byte 0x89 in position 142809: illegal multibyte sequence </details>"""
  
  return viewed_markdown, civitai_html
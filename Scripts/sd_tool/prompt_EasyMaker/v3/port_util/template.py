#version info
#v1/v2 -> v3.0.3

import sys
sys.path.append("..\\")


from LGS.misc import jsonconfig as jsoncfg
from ..modules.shared import ROOT_DIR, DB_PATH, noneimg
from ..modules.lib import save_img, multiple_replace, get_index
from PIL import Image
import os

class variable:
  overwrite = True
  template_data = {
    "example": [
        "v2",
        {
            "Prompt": "%LORA%, %CH_NAME%, %CH_PROMPT%, %LOCATION%, %FACE%, %quality_lite%",
            "Negative": "Negatives"
        },
        [
            "lora_name",
            "character",
            "ch_prompt",
            "location",
            "face",
            "low",
            "head"
        ],
        "C:\\Users\\lunak\\Desktop\\Invisible Files\\luna_py\\luna_py\\Scripts\\sd_tool\\prompt_EasyMaker\\py\\dataset\\image\\example_48241.0.png",
        "48241.0",
        [
            "C:\\Users\\lunak\\Desktop\\Invisible Files\\luna_py\\luna_py\\Scripts\\sd_tool\\prompt_EasyMaker\\py\\dataset\\image\\example_controlnet.png",
            "Lineart",
            0.1,
            "balanced",
            True
        ],
        7.5,
        "FuwaFuwaMix V1.5",
        "512x768",
        "Euler a",
        "Latent"
    ],
    "restainent_lite": [
        {
            "Prompt": "nsfw, %LORA%, small breasts, %CH_NAME%, kneeling, leaning forward, %LOCATION%, solo, 1girl, %FACE%, %CH_PROMPT%, bondage outfit, harness, o-ring, (best quality, masterpiece, detailed, incredibly fine illustration, kawaii) <lora:BondageOutfitV2:0.89>, pussy juice",
            "Negative": "(worst quality:1.4), (low quality:1.4), (normal quality:1.4), (depth of field, blurry:1.2), (greyscale, monochrome:1.1), 3D face, nose, cropped, lowres, text, jpeg artifacts, signature, watermark, username, blurry, artist name, trademark, watermark, ((multiple view)), realistic"
        },
        [
            "None",
            "None",
            "None",
            "None",
            "None"
        ],
        "./dataset/image/None.png",
        "-1"
    ],
    "masturbation_lite": [
        {
            "Prompt": "nsfw, nude, masturbation, pussy, small breasts, pussy juice, nipples, %LORA%, %CH_NAME%, %CH_PROMPT%, (best quality, masterpiece, detailed, incredibly fine illustration, kawaii), 1girl, solo, <lora:masusu_breast:0.8>, <lora:masturbation-v1:1>, %FACE%",
            "Negative": "EasyNegative, (bad anatomy:1.4), (realistic:1.1), (low quality, worst quality:1.1), lips, fat, sad, (inaccurate limb:1.2), (Low resolution:1.1), (((1boy, sex)))"
        },
        [
            "<lora:HoshinoIchika:0.921>",
            "ichika",
            "absorbing long hair, swept bangs, black hair, grey eyes",
            "",
            ""
        ],
        "./dataset/image/masturbation_lite_example.png",
        "1353552248"
    ],
    "masturbation_generator": [
        {
            "Prompt": "<lora:solo_masturbation_normal-masturbation:1.0>, nsfw, masturbation, (best quality, masterpiece, detailed, incredibly fine illustration, kawaii), nsfw, masturbation, fingering, schlick, pussy, pussy juice, trembling, female focus, %FACE%, %LORA%, %CH_NAME%, %CH_PROMPT%, nude, 1girl, %LOCATION%",
            "Negative": "EasyNegative, (bad anatomy:1.4), (realistic:1.1), (low quality, worst quality:1.1), lips, fat, sad, (inaccurate limb:1.2), (Low resolution:1.1), (((1boy, sex)))"
        },
        [
            "<lora:momoi1:0.825>",
            "momoidef",
            "(cute, slim, rori, 12 years old:0.9)",
            "on bed",
            "blush, (orgasm), full blush, wink"
        ],
        "./dataset/image/None.png",
        "SampleImage_Seed"
    ],
    "cute_nake_coat_lite": [
        {
            "Prompt": "nsfw, pink and pastel aqua color gradation and white lines coat, cute cat ears, cat ears, white ribbon on cat ears, naked coat, nude, %FACE%, blush, (white firmer on cuffs), multicolored socks, moesode, pussy, pussy juice, %LORA%, %CH_NAME%, %CH_PROMPT%, <lora:masusu_breast:0.8>, (best quality, masterpiece, detailed, incredibly fine illustration, kawaii), 1girl, solo",
            "Negative": "EasyNegative, (bad anatomy:1.4), (realistic:1.1), (low quality, worst quality:1.1), lips, fat, sad, (inaccurate limb:1.2), (Low resolution:1.1), (((1boy, sex, penis)))"
        },
        [
            "<lora:YoisakiKanade:1.0>",
            "yoka",
            "blue eyes, grey hair, blue hair, long hair, very long hair, hair between eyes",
            "1girl, solo, nsfw, (nude, naked coat, small breasts, bare breasts:1.3)",
            "looking at away, facing at viewer"
        ],
        "./dataset/image/cute_naked_coat_example.png",
        "2140431641"
    ],
    "whb_only_lite": [
        {
            "Prompt": "<lora:whb:1>, nsfw, whb, nude, (best quality, masterpiece, detailed, incredibly fine illustration, kawaii), %FACE%, blush, full body, pussy, pussy juice, nipple, female focus, %LORA%, %CH_NAME%, %CH_PROMPT%, looking at viewer, nude, bare breasts, 14 years old, baby face:0.7, 2dimensional-charactor, trembling, straddling the whb, 1girl",
            "Negative": "EasyNegative, (realistic, low quality, worst quality:1.2), badhandv5"
        },
        [
            "",
            "",
            "",
            "",
            ""
        ],
        "./dataset/image/None.png",
        "SampleImage_Seed"
    ],
    "masturbation_jirasi": [
        {
            "Prompt": "nsfw, %LORA%, %CH_NAME%, %CH_PROMPT%, %FACE%, trembling, nude, %LOCATION%, <lora:masusu_breast:0.835>, naked coat, pussy, pussy juice, nipples, small breasts, no light eyes, arms behind back, (slim, 14 years old, rori:0.95), cat ears, (best quality, masterpiece, detailed, incredibly fine illustration, kawaii)",
            "Negative": "EasyNegative, (bad anatomy:1.4), (realistic:1.1), (low quality, worst quality:1.1), lips, fat, sad, (inaccurate limb:1.2), (Low resolution:1.1), (((1boy, sex)))"
        },
        [
            "<lora:NotKyo:1.0>",
            "nene",
            "long hair, 1girl, purple eyes, green hair, grey hair:0.6",
            "on bed, lying in bed",
            "blush, orgasm, looking at away"
        ],
        "./dataset/image/masturbation_jirasi.png",
        "2561621168"
    ],
    "simply_sample": [
        {
            "Prompt": "%CH_NAME%, %LORA%, %CH_PROMPT%, smile, blush, shy, no background, simple background, white background, standing, looking at viewer, small breasts, slim, masterpiece, best quality, rori, cute, kawaii, white tights, zettai ryouiki,",
            "Negative": "EasyNegative, (realistic, low quality, worst quality:1.2), badhandv5"
        },
        [
            "<lora:nahida1:0.75",
            "nahidadef",
            "1girl, solo",
            "",
            ""
        ],
        "./dataset/image/simply_sample.png",
        "85"
    ],
    "simply_sample_nude": [
        {
            "Prompt": "nude, pussy, nipples, nsfw, pussy juice, %CH_NAME%, %LORA%, %CH_PROMPT%, smile, blush, shy, no background, simple background, white background, standing, looking at viewer, small breasts,slim, masterpiece, best quality, rori, cute, kawaii, <lora:masusu_breast:0.65>, white tights, zettai ryouiki,",
            "Negative": "EasyNegative, (realistic, low quality, worst quality:1.2), badhandv5"
        },
        [
            "<lora:nahida1:0.75",
            "nahidadef",
            "1girl, solo",
            "",
            ""
        ],
        "./dataset/image/simply_sample.png",
        "85"
    ],
    "simple_naked_coat": [
        {
            "Prompt": "%CH_NAME%, %LORA%, 12 years old, %CH_PROMPT%, shy, baby face:0.75, lying on bed, naked coat, white coat, nude, pussy, nipples, small breasts, blush, looking at away, slim, masterpiece, best quality, rori, cute, kawaii, nsfw, white tights, zettai ryouiki, <lora:masusu_breast:0.65>",
            "Negative": "EasyNegative, (realistic, low quality, worst quality:1.2), badhandv5"
        },
        [
            "<lora:nahida1:0.625",
            "nahidadef",
            "1girl, solo",
            "",
            ""
        ],
        "./dataset/image/simple_naked_coat.png",
        "85"
    ],
    "cute_whitegirl": [
        {
            "Prompt": "1girl, solo, cute, kawaii, masterpiece, best quality, looking at viewer, white wing, 12 years old, white hair, aqua eyes, %LOCATION%, %FACE%,",
            "Negative": "EasyNegative, badhandv5, (low quality, worst quality:1.1)"
        },
        [
            "",
            "",
            "",
            "ocean",
            "shy, shy, rori, cat ears"
        ],
        "./dataset/image/None.png",
        "85"
    ],
    "masturbation_orgasm": [
        {
            "Prompt": "nsfw, %LORA%, %CH_NAME%, %FACE%, %LOCATION%, naked coat, white coat, nude, pussy, pussy juice, small nipples, small breasts, blush, looking at away, slim, masterpiece, best quality, rori, cute, kawaii, nsfw, white tights, zettai ryouiki, <lora:masusu_breast:0.65>, %CH_PROMPT%, navel cutout, <lora:stained sheets2:0.525>, stained sheets, <lora:solo_masturbation_normal-masturbation:0.85>, masturbation, female masturbation, hand on pussy, fingering, schlick, trembling, blush, orgasm, one eye closed, ",
            "Negative": "EasyNegative, badhandv5, (bad anatomy:1.4), (realistic:1.1), (low quality, worst quality:1.1), lips, fat, sad, (inaccurate limb:1.2), (Low resolution:1.1), (((1boy, penis))), cat \\(animal\\), animals, cats, cat, black cat, public hair, extra fingers, anal,"
        },
        [
            "<lora:karyl_v1:1.125>",
            "karylaa, karyl, (karyldd)",
            "two-tone hair, low twintails, white veil, hairband, ((green eyes, fang, cat tail, black hair, cat ears)), white ribbon, white dress, white sleeves",
            "lying on bed",
            "shy, baby face:0.75"
        ],
        "./dataset/image/masturbation_orgasm.png",
        "1282158332"
    ],
    "cat_cosplay": [
        {
            "Prompt": "nsfw, %quality_lite%, 1girl, solo, cute, kawaii, (11 years old, baby face:0.97), rori, (cat ears, cat tails, cat cosplay), %LORA%, %CH_NAME%, %CH_PROMPT%, kneeling, cat cosplay, ((1girl, solo)), %FACE%, slim, %LOCATION%,",
            "Negative": "EasyNegative, badhandv5, (bad anatomy:1.4), (realistic:1.1), (low quality, worst quality:1.1), lips, fat, sad, (inaccurate limb:1.2), (Low resolution:1.1), (((1boy, sex))), "
        },
        [
            "<lora:kokkoro_v1:0.95>",
            "",
            "kokkoro",
            "indoor, necklace, nude, pussy, nipples, <lora:masusu_breast:0.65>",
            "blush"
        ],
        "./dataset/image/cat_cosplay-2752216972.png",
        "2752216972"
    ],
    "cheerleader_bluearchive": [
        {
            "Prompt": "<lora:cheerleader_cosplay_bluearchive:0.75>, cheerleader, crop top, miniskirt, bare shoulders, skirt, holding pom poms, pom pom \\(cheerleading\\), %LORA%, %CH_NAME%, %CH_NAME%, %CH_PROMPT%, %LOCATION%, 1girl, solo, slim, %rori%, ",
            "Negative": "EasyNegative, (bad anatomy:1.4), (realistic:1.1), (low quality, worst quality:1.1), lips, fat, sad, (inaccurate limb:1.2), (Low resolution:1.1), (((1boy, sex)))"
        },
        [
            "",
            "",
            "",
            "",
            ""
        ],
        "./dataset/image/cat_cosplay-2752216972.png",
        ""
    ],
    "tentacle_sex (standing)": [
        {
            "Prompt": "nsfw, tentacle insertion, sex, tentacle sex, <lora:chushou:1.195>, (tentacles), tentacles, nipples, small nipples, cowboy shot, sad, (orgasm), blush, wink, %LORA:0.657%, %CH_NAME%, (best quality, masterpiece, detailed, incredibly fine illustration, kawaii), %CH_PROMPT%,",
            "Negative": "EasyNegative, (bad anatomy:1.4), (realistic:1.1), (low quality, worst quality:1.1), lips, fat, sad, (inaccurate limb:1.2), (Low resolution:1.1), (((1boy))), 1 boy,"
        },
        [
            "<lora:hatsune_miku_project_sekai_v1:0.657>",
            "nigomiku",
            "heterochromia, aqua eyes, pink eyes, grey hair, long hair, twintails,",
            "",
            ""
        ],
        "./dataset/image/tentacle_standing_sex-.png",
        ""
    ],
    "tentacle_sex (lying)": [
        {
            "Prompt": "nsfw, lying, tentacle insertion, sex, tentacle sex, <lora:chushou:1.195>, (tentacles), tentacles, nipples, small nipples, sad, (orgasm), blush, wink, %LORA%:0.657, %CH_NAME%, (best quality, masterpiece, detailed, incredibly fine illustration, kawaii), %CH_PROMPT%,",
            "Negative": "EasyNegative, (bad anatomy:1.4), (realistic:1.1), (low quality, worst quality:1.1), lips, fat, sad, (inaccurate limb:1.2), (Low resolution:1.1), (((1boy))), 1 boy,"
        },
        [
            "<lora:hatsune_miku_project_sekai_v1:0.657>",
            "nigomiku",
            "heterochromia, aqua eyes, pink eyes, grey hair, long hair, twintails,",
            "",
            ""
        ],
        "./dataset/image/tentacle_lying_sex-551439590.png",
        "551439590"
    ],
    "character lora tester": [
        {
            "Prompt": "%CH_NAME%, %LORA%, %CH_PROMPT%, %FACE%, %LOCATION%, %quality_lite%,",
            "Negative": "EasyNegative, badhandv5, (bad anatomy, low quality, worst quaity:1.345),"
        },
        [
            "<lora:YoisakiKanade:0.895>",
            "yoka",
            "blue eyes, grey hair, blue hair, long hair, very long hair, hair between eyes",
            "simple background",
            "shy"
        ],
        "./dataset/image/None.png",
        "-1"
    ],
    "mmj_idol": [
        {
            "Prompt": "%quality_lite%, (skirt, layered skirt, piano design skirt, miniskirt, frill skirt, frills, frilled skirt:1.1), sleeveless, frill, hair ornament, frills, necktie, frilled_skirt, %CH_PROMPT%, white cloth, idol, black belt, yellow belt, clover, ornament, orange cloth, white skirt, white frilled skirt, slim, tightly fitting cloth, %FACE%, %LORA%, %CH_NAME%, cute, slim legs, slim arms, %LOCATION%, ",
            "Negative": "EasyNegative, badhandv5, (bad anatomy:1.4), (realistic:1.1), (low quality, worst quality:1.1), lips, fat, sad, (inaccurate limb:1.2), "
        },
        [
            "<lora:HanasatoMinori:0.675>",
            "minori",
            "brown hair, grey eyes, medium hair",
            "",
            "smile, idol, cute, 1girl, solo"
        ],
        "./dataset/image/None.png",
        "-1"
    ],
    "naked ribbon": [
        {
            "Prompt": "nsfw, %quality_lite%, <lora:NakedRibbon:0.85>, naked ribbon, naked_ribbon, ribbon, %LORA%, %CH_NAME%, nude, %FACE%, %LOCATION%, topless, bow, absurdres, pussy, %CH_PROMPT%",
            "Negative": "EasyNegative, badhandv5, (bad anatomy:1.4), (realistic:1.1), (low quality, worst quality:1.1), lips, fat, sad, (inaccurate limb:1.2), (Low resolution:1.1), lowres, poorly drawn, monochrome"
        },
        [
            "",
            "kyouka",
            "halloween, light purple hair, twintails, long hair, 10 years old, yellow eyes",
            "indoor, lying on bed, on bed",
            "blush, looking at away, shy"
        ],
        "./dataset/image/None.png",
        "0"
    ],
    "tentacle_fellatio_pov": [
        {
            "Prompt": "nsfw, ((suck tentacle, tentacle fellatio, fellatio:1.25)), <lora:chushou:1.195>, (tentacles), tentacles, pov, 1girl, solo, tentacle sex, tentacle insertion, touch tentacles, %FACE%, %LORA%, %CH_NAME%, %CH_PROMPT%, (best quality, masterpiece:1.25),",
            "Negative": "EasyNegative, badhandv5, (bad anatomy:1.4), (realistic:1.1), (low quality, worst quality:1.1), lips, fat, sad, (inaccurate limb:1.2), (Low resolution:1.1), (((1boy))), 1boy, public hair,"
        },
        [
            "",
            "",
            "",
            "",
            ""
        ],
        "./dataset/image/None.png",
        "0"
    ],
    "tentacle_fellatio_from_side": [
        {
            "Prompt": "nsfw, lying, ((suck tentacle, tentacle fellatio, fellatio:1.25)), <lora:chushou:1.195>, from side, side view, (tentacles insertion, tentacle sex:1.175), (tentacles), tentacles, tentacle sex, tentacle insertion, %FACE%, %LORA%, %CH_NAME%, %CH_PROMPT%, (best quality, masterpiece:1.25), from side, side view, 1girl",
            "Negative": "EasyNegative, badhandv5, (bad anatomy:1.4), (realistic:1.1), (low quality, worst quality:1.1), lips, fat, sad, (inaccurate limb:1.2), (Low resolution:1.1), (((1boy))), 1boy, public hair, multiple view, "
        },
        [
            "",
            "",
            "",
            "",
            ""
        ],
        "./dataset/image/None.png",
        "0"
    ],
    "ichika - backarm shibari": [
        "v2",
        {
            "Prompt": "bound, bdsm, bondage, rope, shibari, %LORA:0.675%, %CH_NAME%, blush, %FACE%, pussy, sitting, bound legs, arms behind back, thighs, %CH_PROMPT%, tied_up, bound arms, %LOCATION%, facial, messy hair, snowing, restrained, full body, kneeling, nsfw, (white semi-transpert fluid in pussy, white semi-transpert fluid on lower body, white semi-transpert fluid on thighs:0.725) ",
            "Negative": "mosaic, mosaic on pussy, nsfw censor, mosaic censored, EasyNegative, (bad anatomy:1.4), (realistic:1.1), (low quality, worst quality:1.1), lips, fat, (inaccurate limb:1.2), (Low resolution:1.1), (((1boy, penis))), (transpert pussy juice:-1.0)"
        },
        [
            "<lora:HoshinoIchika:0.675>",
            "ichika",
            "absorbing long hair, swept bangs, black hair, grey eyes",
            "outdoor, 1girl, solo, snow, winter, snowing",
            "blush, sad, tears, looking at viewer, cute, collarbone",
            "nude, (transpert pussy juice, pussy juice, small nipples, nipples, medium breasts, pussy:1.125), open_mouth, %quality_lite%,",
            "nsfw"
        ],
        "./dataset/image/None.png",
        "0.0",
        [
            "C:\\Users\\lunak\\Desktop\\Invisible Files\\luna_py\\luna_py\\Scripts\\sd_tool\\prompt_EasyMaker\\py\\dataset\\image\\ichika - backarm shibari_controlnet.png",
            "Lineart",
            0.2,
            "balanced",
            False
        ],
        8,
        "FuwaFuwaMix V1.5",
        "1024x1536",
        "\u753b\u8cea\u306f 512x768 \u304b\u3089 Hires.fix \u306e Upscale x2 \u306b\u3059\u308b\u3068\u3044\u3046\u624b\u3082\u3042\u308a\u3002\u3057\u304b\u3057\u305d\u306e\u5834\u5408\u306fControlNet\u306e Pixel Perfect \u3092\u30aa\u30d5\u306b",
        ""
    ],
    "tentacle clothes v1": [
        "v2",
        {
            "Prompt": "nsfw, <lora:tentacle_clothes:0.95>, (tentacle clothes:1.375), (tentacles), trembling, close one eye, open mouth, ((orgasm)), nipples, small nipples, cowboy shot, %FACE%, blush, wink, %LORA:0.75%, %CH_NAME%, %LOCATION%, %quality_lite%, 1girl, solo, %CH_PROMPT%, <lora:chushou111:0.25>, <lora:masusu_breast:0.5>",
            "Negative": "mosaic, mosaic on pussy, nsfw censor, mosaic censored, EasyNegative, (bad anatomy:1.4), (realistic:1.1), (low quality, worst quality:1.1), lips, fat, (inaccurate limb:1.2), (Low resolution:1.1), (((1boy, penis))), (transpert pussy juice:-1.0)"
        },
        [
            "<lora:HanasatoMinori:0.75>",
            "minori",
            "brown hair, grey eyes, medium hair",
            "ocean. open beach",
            "sad, (orgasm), blush",
            "(tentacle cum in pussy, tentacle cum on thights:0.875), pussy juice, transpert pussy juice, bikini, bare breasts, miniskirt, frill, frilled miniskirt,",
            ""
        ],
        "C:\\Users\\lunak\\Desktop\\Invisible Files\\luna_py\\luna_py\\Scripts\\sd_tool\\prompt_EasyMaker\\py\\dataset\\image\\tentacle clothes v1_0.0.png",
        "0.0",
        [
            "./dataset/image/None.png",
            "",
            0.5,
            "",
            False
        ],
        8,
        "HassakuHentaiModel",
        "512x768",
        "Euler a",
        "Latent (nearest)"
    ],
    "\u898b\u305b\u306a\u3044\u69cb\u56f3 v1 - ControlNet": [
        "v2",
        {
            "Prompt": "1girl, (nsfw:0.15), knees together feet apart, facing viewer, hands on own knees, from above, %FACE%, %LOCATION%, %LORA:0.675%, %CH_NAME%, %CH_PROMPT%, %quality_lite%,",
            "Negative": ""
        },
        [
            "",
            "",
            "",
            "sitting on floor, against wall",
            "bare foot",
            "",
            ""
        ],
        "./dataset/image/None.png",
        "0.0",
        [
            "C:\\Users\\lunak\\Desktop\\Invisible Files\\luna_py\\luna_py\\Scripts\\sd_tool\\prompt_EasyMaker\\py\\dataset\\image\\\u898b\u305b\u306a\u3044\u69cb\u56f3 v1 - ControlNet_controlnet.png",
            "OpenPose",
            0.85,
            "balanced",
            False
        ],
        7,
        "",
        "512x768",
        "",
        ""
    ],
    "\u898b\u305b\u306a\u3044\u69cb\u56f3 v2 - ControlNet": [
        "v2",
        {
            "Prompt": "1girl, (nsfw:0.15), knees together feet apart, facing viewer, hands on own knees, bare foot, sitting, %FACE%, %LOCATION%, %LORA:0.675%, %CH_NAME%, %CH_PROMPT%, %quality_lite%,",
            "Negative": "EasyNegative, (bad anatomy:1.4), (realistic:1.1), (low quality, worst quality:1.1), lips, fat, sad, (inaccurate limb:1.2), (Low resolution:1.1), (((1boy, penis))), pussy,"
        },
        [
            "",
            "",
            "",
            "against wall",
            "",
            "",
            ""
        ],
        "C:\\Users\\lunak\\Desktop\\Invisible Files\\luna_py\\luna_py\\Scripts\\sd_tool\\prompt_EasyMaker\\py\\dataset\\image\\\u898b\u305b\u306a\u3044\u69cb\u56f3 v2 - ControlNet_0.0.png",
        "0.0",
        [
            "C:\\Users\\lunak\\Desktop\\Invisible Files\\luna_py\\luna_py\\Scripts\\sd_tool\\prompt_EasyMaker\\py\\dataset\\image\\\u898b\u305b\u306a\u3044\u69cb\u56f3 v2 - ControlNet_controlnet.png",
            "OpenPose",
            0.9,
            "balanced",
            False
        ],
        7,
        "",
        "512x768",
        "",
        ""
    ],
    "Leaning Forward (Basic) - ControlNet": [
        "v2",
        {
            "Prompt": "%quality_lite%, %LOCATION%, %CH_PROMPT%, leaning forward, %CH_NAME%, %LORA:0.75%, %FACE%",
            "Negative": ""
        },
        [
            "",
            "",
            "",
            "",
            "",
            "",
            ""
        ],
        "C:\\Users\\lunak\\Desktop\\Invisible Files\\luna_py\\luna_py\\Scripts\\sd_tool\\prompt_EasyMaker\\py\\dataset\\image\\Leaning Forward (Basic) - ControlNet_0.0.png",
        "0.0",
        [
            "C:\\Users\\lunak\\Desktop\\Invisible Files\\luna_py\\luna_py\\Scripts\\sd_tool\\prompt_EasyMaker\\py\\dataset\\image\\Leaning Forward (Basic) - ControlNet_controlnet.png",
            "OpenPose",
            0.75,
            "balanced",
            False],
        7,
        "FuwaFuwaMix V1.5",
        "512x768",
        "",
        ""
    ],
    "Sitting (Basic) - ControlNet": [
        "v2",
        {
            "Prompt": "sitting on object, %LOCATION%, %FACE%, %CH_PROMPT%, %LORA:0.7%, %CH_NAME%",
            "Negative": ""
        },
        [
            "",
            "",
            "",
            "",
            "",
            "",
            ""
        ],
        "C:\\Users\\lunak\\Desktop\\Invisible Files\\luna_py\\luna_py\\Scripts\\sd_tool\\prompt_EasyMaker\\py\\dataset\\image\\Sitting (Basic) - ControlNet_0.0.png",
        "0.0",
        [
            "C:\\Users\\lunak\\Desktop\\Invisible Files\\luna_py\\luna_py\\Scripts\\sd_tool\\prompt_EasyMaker\\py\\dataset\\image\\Sitting (Basic) - ControlNet_controlnet.png",
            "OpenPose",
            0.75,
            "balanced",
            False
        ],
        7,
        "FuwaFuwaMix V1.5",
        "512x768",
        "",
        ""
    ],
    "Crossed Arms (Basic) - ControlNet": [
        "v2",
        {
            "Prompt": "crossed arms, %LOCATION%, %FACE%, %CH_PROMPT%, %LORA:0.7%, %CH_NAME%",
            "Negative": ""
        },
        [
            "",
            "",
            "",
            "",
            "",
            "",
            ""
        ],
        "C:\\Users\\lunak\\Desktop\\Invisible Files\\luna_py\\luna_py\\Scripts\\sd_tool\\prompt_EasyMaker\\py\\dataset\\image\\Crossed Arms (Basic) - ControlNet_0.0.png",
        "0.0",
        [
            "C:\\Users\\lunak\\Desktop\\Invisible Files\\luna_py\\luna_py\\Scripts\\sd_tool\\prompt_EasyMaker\\py\\dataset\\image\\Crossed Arms (Basic) - ControlNet_controlnet.png",
            "OpenPose",
            0.75,
            "balanced",
            False
        ],
        7,
        "FuwaFuwaMix V1.5",
        "512x768",
        "",
        ""
    ],
    "Hugging own legs (Basic) - ControlNet": [
        "v2",
        {
            "Prompt": "hugging own legs, bare foot, sitting, %LOCATION%, %FACE%, %CH_PROMPT%, %LORA:0.7%, %CH_NAME%, sitting",
            "Negative": ""
        },
        [
            "",
            "",
            "",
            "",
            "",
            "",
            ""
        ],
        "C:\\Users\\lunak\\Desktop\\Invisible Files\\luna_py\\luna_py\\Scripts\\sd_tool\\prompt_EasyMaker\\py\\dataset\\image\\Hugging own legs (Basic) - ControlNet_0.0.png",
        "0.0",
        [
            "C:\\Users\\lunak\\Desktop\\Invisible Files\\luna_py\\luna_py\\Scripts\\sd_tool\\prompt_EasyMaker\\py\\dataset\\image\\Hugging own legs (Basic) - ControlNet_controlnet.png",
            "OpenPose",
            0.75,
            "balanced",
            False
        ],
        7,
        "FuwaFuwaMix V1.5",
        "512x768",
        "",
        ""
    ],
    "Lying (sleeping) (Basic) - ControlNet": [
        "v2",
        {
            "Prompt": "from above, fetal position, bare legs, lying, bare foot, %LOCATION%, %FACE%, %CH_PROMPT%, %LORA:0.7%, %CH_NAME%",
            "Negative": ""
        },
        [
            "",
            "",
            "",
            "",
            "",
            "",
            ""
        ],
        "C:\\Users\\lunak\\Desktop\\Invisible Files\\luna_py\\luna_py\\Scripts\\sd_tool\\prompt_EasyMaker\\py\\dataset\\image\\Lying (sleeping) (Basic) - ControlNet_0.0.png",
        "0.0",
        [
            "C:\\Users\\lunak\\Desktop\\Invisible Files\\luna_py\\luna_py\\Scripts\\sd_tool\\prompt_EasyMaker\\py\\dataset\\image\\Lying (sleeping) (Basic) - ControlNet_controlnet.png",
            "OpenPose",
            0.8,
            "balanced",
            False
        ],
        7,
        "FuwaFuwaMix V1.5",
        "512x768",
        "",
        ""
    ],
    "Head Rest - Double arms (Basic) - ControlNet": [
        "v2",
        {
            "Prompt": "sitting, hand on own cheek, head rest, looking at viewers, %LOCATION%, %FACE%, %CH_PROMPT%, %LORA:0.7%, %CH_NAME%",
            "Negative": ""
        },
        [
            "",
            "",
            "",
            "",
            "",
            "",
            ""
        ],
        "C:\\Users\\lunak\\Desktop\\Invisible Files\\luna_py\\luna_py\\Scripts\\sd_tool\\prompt_EasyMaker\\py\\dataset\\image\\Head Rest - Double arms (Basic) - ControlNet_0.0.png",
        "0.0",
        [
            "C:\\Users\\lunak\\Desktop\\Invisible Files\\luna_py\\luna_py\\Scripts\\sd_tool\\prompt_EasyMaker\\py\\dataset\\image\\Head Rest - Double arms (Basic) - ControlNet_controlnet.png",
            "OpenPose",
            0.8,
            "balanced",
            False
        ],
        7,
        "FuwaFuwaMix V1.5",
        "512x768",
        "",
        ""
    ],
    "Head Rest - Single arms (Basic) - ControlNet": [
        "v2",
        {
            "Prompt": "sitting, one hand on own cheek, head rest, looking at viewers, %LOCATION%, %FACE%, %CH_PROMPT%, %LORA:0.7%, %CH_NAME%",
            "Negative": ""
        },
        [
            "",
            "",
            "",
            "",
            "",
            "",
            ""
        ],
        "C:\\Users\\lunak\\Desktop\\Invisible Files\\luna_py\\luna_py\\Scripts\\sd_tool\\prompt_EasyMaker\\py\\dataset\\image\\Head Rest - Single arms (Basic) - ControlNet_0.0.png",
        "0.0",
        [
            "C:\\Users\\lunak\\Desktop\\Invisible Files\\luna_py\\luna_py\\Scripts\\sd_tool\\prompt_EasyMaker\\py\\dataset\\image\\Head Rest - Single arms (Basic) - ControlNet_controlnet.png",
            "OpenPose",
            0.8,
            "balanced",
            False
        ],
        7,
        "FuwaFuwaMix V1.5",
        "512x768",
        "",
        ""
    ],
    "Wariza (Basic) - ControlNet": [
        "v2",
        {
            "Prompt": "wariza, %LOCATION%, %FACE%, %CH_PROMPT%, %LORA:0.7%, %CH_NAME%",
            "Negative": ""
        },
        [
            "",
            "",
            "",
            "",
            "",
            "",
            ""
        ],
        "C:\\Users\\lunak\\Desktop\\Invisible Files\\luna_py\\luna_py\\Scripts\\sd_tool\\prompt_EasyMaker\\py\\dataset\\image\\Wariza (Basic) - ControlNet_0.0.png",
        "0.0",
        [
            "C:\\Users\\lunak\\Desktop\\Invisible Files\\luna_py\\luna_py\\Scripts\\sd_tool\\prompt_EasyMaker\\py\\dataset\\image\\Wariza (Basic) - ControlNet_controlnet.png",
            "OpenPose",
            0.75,
            "balanced",
            False
        ],
        7,
        "FuwaFuwaMix V1.5",
        "512x768",
        "",
        ""
    ]
  }
  full_access = True
  
def main(fp):
  already_data = jsoncfg.read(
    os.path.join(DB_PATH, "template_list.json"))
  
  # 処理
  for key, dates in variable.template_data.values():
    # key の重複を回避
    if key in already_data.keys():
      if variable.overwrite:
        pass
      else:
        key = key+" (v1 template)"
        while key in already_data.keys():
          key += "_"
    
    if len(dates) == 4 or dates[0] == "v1":
      version = "v1"
      prompt = dates[0]["Prompt"]
      negative = dates[0]["Negative"]
      example_data = dates[1] + ["", ""] # header, lower を空の状態で追加
      image_path = dates[2]
      seed = dates[3]
      enabled_cn = False
      cn_data = []
      v2opts = []
    
    else: # v2
      version = dates[0]
      prompt = dates[1]["Prompt"]
      negative = dates[1]["Negative"]
      example_data = dates[2]
      image_path = dates[3]
      seed = dates[4]
      
      # V v2 method
      cn_data = dates[5]
      cn_image = cn_data[0]
      cfg_scale = dates[6]
      sdcp = dates[7]
      resolution = dates[8]
      sampler = dates[9]
      hires_method = dates[10]
      v2opts = [resolution, sampler, hires_method, cfg_scale]

      enabled_cn = False
      if cn_image != "./dataset/image/None.png":
        enabled_cn = True
        
    # image check
    
    
    def img_check(image_path, iscn):
      if variable.full_access:
        if os.path.exists(image_path):
          if image_path == "./dataset/image/None.png":
            images = None
          else:
            images = Image.open(image_path)
        else:
          images = None
      else:
        images = None
          
      # v3.0.6+ relpath
      if images is None:
        img = noneimg
      else:
        img = f"image/{iscn}{key}.png"
        save_img(img, images)
      return img

    img_path = img_check(image_path, "")
    if version == "v2":
      cn_path = img_check(cn_image, "cn_")
    
    # Prompt
    prompt = multiple_replace(
      prompt, [
        ("%LORA%", "$LORA"), ("%CH_NAME%", "$NAME"), ("%CH_PROMPT%", "$PROMPT"),
        ("%FACE", "$FACE"), ("%LOCATION%", "$LOCATION"), ("%quality_lite%", "(masterpiece, best quality:1.2)")
      ]
    )    
    
    
    # 変換
    dicts = {
      "Method": "v3.0.3",
      "Method_Release": 3,
      "Key": key,
      "Values": {
        "Prompt": prompt,
        "Negative": negative,
        "AD_Prompt": "DISABLED",
        "AD_Negative": "DISABLED"
      },
      "ControlNet": {
        "isEnabled": enabled_cn,
        "Mode": get_index(cn_data, 1, "null"),
        "Weight": get_index(cn_data, 2, 0),
        "Image": cn_path
      },
      "Example": {
        "isEnabled": True,
        "Character": "",
        "Lora": example_data[0],
        "Name": example_data[1],
        "Prompt": example_data[2],
        "isExtend": False,
        "Face": example_data[4],
        "Location": example_data[3],
        "Header": example_data[5],
        "Lower": example_data[6],
        "Image": img_path,
        "CustomNegative": "Ported with port_util:template.py:main"
      },
      "Resolution": get_index(v2opts, 0, "0×0"),
      "Sampler": get_index(v2opts, 1, "null"),
      "Clip": 2.0,
      "displayName": key,
      "DatabaesPath": None,
      "CFG": get_index(v2opts, 3, 7),
      "images": None,
      "Regional_Prompter": {
            "isEnabled": False,
            "rp_mode": "Matrix",
            "Secondary_Prompt": {
                "prompt": "",
                "characters": "",
                "weight": 0.75,
                "lora": "",
                "name": "",
                "ch_prompt": "",
                "face": "",
                "location": "",
                "header": "",
                "lower": "",
                "gFaL_from_Main": False
            },
            "mode": "Attention",
            "base": False,
            "common": [
                True,
                True
            ],
            "lora_stop_step": [
                0,
                0
            ],
            "resolution": [
                512,
                512
            ],
            "split_mode": "Columns",
            "split_ratio": "1:1",
            "base_ratio": 0.2
        },
      "Hires": {
            "isEnabled": False,
            "Upscale": 2.0,
            "Sampler": "R-ESRGAN 4x+ Anime6B",
            "Denoising": 0.45,
            "Steps": 8
        }
    }
  
if __name__ == "__main__":
  main(None)
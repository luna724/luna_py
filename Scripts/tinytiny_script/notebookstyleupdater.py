## Driveからモデルの取得
#if Download_prcn_style:
#  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/prcn_style.safetensors" "/content/stable-diffusion-webui/models/Lora/prcn_style.safetensors"
#if Download_yuni_prcn:
#  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/yuni_prcn.safetensors" "/content/stable-diffusion-webui/models/Lora/yuni_prcn.safetensors"

target_string = """
if Download_prcn_style:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/prcn_style.safetensors" "/content/stable-diffusion-webui/models/Lora/prcn_style.safetensors"
if Download_yuni_prcn:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/yuni_prcn.safetensors" "/content/stable-diffusion-webui/models/Lora/yuni_prcn.safetensors"
if Download_gochiusa_pack:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/gochiusa_pack.safetensors" "/content/stable-diffusion-webui/models/Lora/gochiusa_pack.safetensors"
if Download_KomorebiMix_v1:
  !cp -r "/content/gdrive/MyDrive/SD_Model/komorebimix_v1.safetensors" "/content/stable-diffusion-webui/models/Stable-diffusion/komorebimix_v1.safetensors"
if Download_KomorebiMix_v12:
  !cp -r "/content/gdrive/MyDrive/SD_Model/komorebimix_v12.safetensors" "/content/stable-diffusion-webui/models/Stable-diffusion/komorebimix_v12.safetensors"
if Download_after_kiss:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/after_kiss.safetensors" "/content/stable-diffusion-webui/models/Lora/after_kiss.safetensors"
if Download_bunny_pose:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/bunny_pose.safetensors" "/content/stable-diffusion-webui/models/Lora/bunny_pose.safetensors"
if Download_Kagamine_rin:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/kagamine_rin.safetensors" "/content/stable-diffusion-webui//models/Lora/kagamine_rin.safetensors"
if Download_Flandre_scarlet_usami:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/flandre_scarlet_usami.safetensors" "/content/stable-diffusion-webui//models/Lora/flandre_scarlet_usami.safetensors"
if Download_Flandre_scarlet_narugo:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/flandre_scarlet_narugo.safetensors" "/content/stable-diffusion-webui//models/Lora/flandre_scarlet_narugo.safetensors"
if Download_Flandre_scarlet_narugo:
  !cp -r "/content/gdrive/MyDrive/SD_Model/Texture_Inversion/flandre_scarlet_narugo.pt" "/content/stable-diffusion-webui//embeddings/flandre_scarlet_narugo.pt"
if Download_moriya_suwako_narugo:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/moriya_suwako_narugo.safetensors" "/content/stable-diffusion-webui//models/Lora/moriya_suwako_narugo.safetensors"
if Download_moriya_suwako_narugo:
  !cp -r "/content/gdrive/MyDrive/SD_Model/Texture_Inversion/moriya_suwako_narugo.pt" "/content/stable-diffusion-webui//embeddings/moriya_suwako_narugo.pt"
if Download_hatano_kokoro_narugo:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/hatano_kokoro_narugo.safetensors" "/content/stable-diffusion-webui//models/Lora/hatano_kokoro_narugo.safetensors"
if Download_hatano_kokoro_narugo:
  !cp -r "/content/gdrive/MyDrive/SD_Model/Texture_Inversion/hatano_kokoro_narugo.pt" "/content/stable-diffusion-webui//embeddings/hatano_kokoro_narugo.pt"
if Download_komeiji_koishi_narugo:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/komeiji_koishi_narugo.safetensors" "/content/stable-diffusion-webui//models/Lora/komeiji_koishi_narugo.safetensors"
if Download_komeiji_koishi_narugo:
  !cp -r "/content/gdrive/MyDrive/SD_Model/Texture_Inversion/komeiji_koishi_narugo.pt" "/content/stable-diffusion-webui//embeddings/komeiji_koishi_narugo.pt"
if Download_reisa_BlueArchive:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/reisa_bluearchive.safetensors" "/content/stable-diffusion-webui//models/Lora/reisa_bluearchive.safetensors"
if Download_reisa_BlueArchive:
  !cp -r "/content/gdrive/MyDrive/SD_Model/Texture_Inversion/reisa_bluearchive.pt" "/content/stable-diffusion-webui//embeddings/reisa_bluearchive.pt"
if Download_rumia_touhou:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/rumia_touhou.safetensors" "/content/stable-diffusion-webui//models/Lora/rumia_touhou.safetensors"
if Download_rumia_touhou:
  !cp -r "/content/gdrive/MyDrive/SD_Model/Texture_Inversion/rumia_touhou.pt" "/content/stable-diffusion-webui//embeddings/rumia_touhou.pt"
if Download_cirno_touhou:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/cirno_touhou.safetensors" "/content/stable-diffusion-webui//models/Lora/cirno_touhou.safetensors"
if Download_cirno_touhou:
  !cp -r "/content/gdrive/MyDrive/SD_Model/Texture_Inversion/cirno_touhou.pt" "/content/stable-diffusion-webui//embeddings/cirno_touhou.pt"
if Download_yakumo_chen:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/yakumo_chen.safetensors" "/content/stable-diffusion-webui//models/Lora/yakumo_chen.safetensors"
if Download_hakurei_reimu:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/hakurei_reimu.safetensors" "/content/stable-diffusion-webui//models/Lora/hakurei_reimu.safetensors"
if Download_komeiji_satori_narugo:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/komeiji_satori_narugo.safetensors" "/content/stable-diffusion-webui//models/Lora/komeiji_satori_narugo.safetensors"
if Download_komeiji_satori_narugo:
  !cp -r "/content/gdrive/MyDrive/SD_Model/Texture_Inversion/komeiji_satori_narugo.pt" "/content/stable-diffusion-webui//embeddings/komeiji_satori_narugo.pt"
if Download_remilia_scarlet_narugo:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/remilia_scarlet_narugo.safetensors" "/content/stable-diffusion-webui//models/Lora/remilia_scarlet_narugo.safetensors"
if Download_remilia_scarlet_narugo:
  !cp -r "/content/gdrive/MyDrive/SD_Model/Texture_Inversion/remilia_scarlet_narugo.pt" "/content/stable-diffusion-webui//embeddings/remilia_scarlet_narugo.pt"
if Download_uzuki_kantai:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/uzuki_kantai.safetensors" "/content/stable-diffusion-webui//models/Lora/uzuki_kantai.safetensors"
if Download_uzuki_kantai:
  !cp -r "/content/gdrive/MyDrive/SD_Model/Texture_Inversion/uzuki_kantai.pt" "/content/stable-diffusion-webui//embeddings/uzuki_kantai.pt"
if Download_clownpiece_touho:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/clownpiece_touho.safetensors" "/content/stable-diffusion-webui//models/Lora/clownpiece_touho.safetensors"
if Download_Kokkoro_prcn:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/kokkoro_prcn.safetensors" "/content/stable-diffusion-webui/models/Lora/kokkoro_prcn.safetensors"
if Download_Kyouka_prcn:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/kyouka_prcn.safetensors" "/content/stable-diffusion-webui/models/Lora/kyouka_prcn.safetensors"
if Download_CuteYukiMix_EchoDimension:
  !cp -r "/content/gdrive/MyDrive/SD_Model/cuteyukimix_echodimension.safetensors" "/content/stable-diffusion-webui/models/Stable-diffusion/cuteyukimix_echodimension.safetensors"
if Download_CuteYukiMix_Kawa_Show:
  !cp -r "/content/gdrive/MyDrive/SD_Model/cuteyukimix_kawa_show.safetensors" "/content/stable-diffusion-webui/models/Stable-diffusion/cuteyukimix_kawa_show.safetensors"
if Download_CuteYukiMix_v4:
  !cp -r "/content/gdrive/MyDrive/SD_Model/cuteyukimix_v4.safetensors" "/content/stable-diffusion-webui/models/Stable-diffusion/cuteyukimix_v4.safetensors"
if Download_CuteYukiMix_NeoChapter2:
  !cp -r "/content/gdrive/MyDrive/SD_Model/cuteyukimix_neochapter2.safetensors" "/content/stable-diffusion-webui/models/Stable-diffusion/cuteyukimix_neochapter2.safetensors"
if Download_CuteYukiMix_MidChapter2_vae:
  !cp -r "/content/gdrive/MyDrive/SD_Model/VAE/cuteyukimix_midchapter2_vae.vae.pt" "/content/stable-diffusion-webui/models/Stable-diffusion/cuteyukimix_midchapter2_vae.pt"
if Download_CuteYukiMix_MidChapter2:
  !cp -r "/content/gdrive/MyDrive/SD_Model/cuteyukimix_midchapter2.safetensors" "/content/stable-diffusion-webui/models/Stable-diffusion/cuteyukimix_midchapter2.safetensors"
if Download_CuteYukiMix_MidChapter3:
  !cp -r "/content/gdrive/MyDrive/SD_Model/cuteyukimix_midchapter3.safetensors" "/content/stable-diffusion-webui/models/Stable-diffusion/cuteyukimix_midchapter3.safetensors"
if Download_COCOtiFaCute:
  !cp -r "/content/gdrive/MyDrive/SD_Model/cocotifacute.safetensors" "/content/stable-diffusion-webui/models/Stable-diffusion/cocotifacute.safetensors"
if Download_Project_K:
  !cp -r "/content/gdrive/MyDrive/SD_Model/project_k.safetensors" "/content/stable-diffusion-webui/models/Stable-diffusion/project_k.safetensors"
if Download_MinaiMix:
  !cp -r "/content/gdrive/MyDrive/SD_Model/minaimix.safetensors" "/content/stable-diffusion-webui/models/Stable-diffusion/minaimix.safetensors"
if Download_FuwaFuwaMix_v15_with_vae:
  !cp -r "/content/gdrive/MyDrive/SD_Model/fuwafuwamix_v15_with_vae.safetensors" "/content/stable-diffusion-webui/models/Stable-diffusion/fuwafuwamix_v15_with_vae.safetensors"
if Download_FuwaFuwaMix_v15:
  !cp -r "/content/gdrive/MyDrive/SD_Model/fuwafuwamix_v15.safetensors" "/content/stable-diffusion-webui/models/Stable-diffusion/fuwafuwamix_v15.safetensors"
if Download_DorayakiMix_v1:
  !cp -r "/content/gdrive/MyDrive/SD_Model/dorayakimix_v1.safetensors" "/content/stable-diffusion-webui/models/Stable-diffusion/dorayakimix_v1.safetensors"
if Download_DorayakiMix_v2_fp16:
  !cp -r "/content/gdrive/MyDrive/SD_Model/dorayakimix_v2_fp16.safetensors" "/content/stable-diffusion-webui/models/Stable-diffusion/dorayakimix_v2_fp16.safetensors"
if Download_DorayukiMix_v3_fp16:
  !cp -r "/content/gdrive/MyDrive/SD_Model/dorayukimix_v3_fp16.safetensors" "/content/stable-diffusion-webui/models/Stable-diffusion/dorayukimix_v3_fp16.safetensors"
if Download_SakuramochiMix:
  !cp -r "/content/gdrive/MyDrive/SD_Model/sakuramochimix.safetensors" "/content/stable-diffusion-webui/models/Stable-diffusion/sakuramochimix.safetensors"
if Download_Sakurai_nozomi_prcn:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/sakurai_nozomi_prcn.safetensors" "/content/stable-diffusion-webui/models/Lora/sakurai_nozomi_prcn.safetensors"
if Download_prcn_style:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/prcn_style.safetensors" "/content/stable-diffusion-webui/models/Lora/prcn_style.safetensors"
if Download_Orangemix_vae:
  !cp -r "/content/gdrive/MyDrive/SD_Model/VAE/orangemix_vae.vae.pt" "/content/stable-diffusion-webui/models/Stable-diffusion/orangemix_vae.pt"
if Download_Anything_v3_vae:
  !cp -r "/content/gdrive/MyDrive/SD_Model/VAE/anything_v3_vae.vae.pt" "/content/stable-diffusion-webui/models/Stable-diffusion/anything_v3_vae.pt"
if Download_test_VAE_vae:
  !cp -r "/content/gdrive/MyDrive/SD_Model/VAE/test_vae_vae.vae.pt" "/content/stable-diffusion-webui/models/Stable-diffusion/test_vae_vae.pt"
if Download_Detail_Tweaker:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/Detail_tweaker_lora.safetensors" "/content/stable-diffusion-webui/models/Lora/Detail_tweaker_lora.safetensors"
if Download_CatCat_XL_AnimeStyle_SDXL:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/CatCat_XL_SDXL.safetensors" "/content/stable-diffusion-webui/models/Lora/CatCat_XL_SDXL.safetensors"
if Download_Slime_girl_16_NeutronSlime_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/slime_girl16_NeutronSlime.safetensors" "/content/stable-diffusion-webui/models/Lora/slime_girl16_NeutronSlime.safetensors"
if Download_Slime_girl_11_NeutronSlime_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/slime_girl11_NeutronSlime.safetensors" "/content/stable-diffusion-webui/models/Lora/slime_girl11_NeutronSlime.safetensors"
if Download_Slime_girl_momoura_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/Slime_girl_momoura.safetensors" "/content/stable-diffusion-webui/models/Lora/Slime_girl_momoura.safetensors"
if Download_Furnace_75v1_Cu6:
  !cp -r "/content/gdrive/MyDrive/SD_Model/furnace_75v1cu6_cutestyle.safetensors" "/content/stable-diffusion-webui/models/Stable-diffusion/furnace_75v1cu6_cutestyle.safetensors"
if Download_Sketch_Inpaint_v20:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/Sketch_impasto_cute_style.safetensors" "/content/stable-diffusion-webui/models/Lora/Sketch_impasto_cute_style.safetensors"
if Download_pose_mutual_Masturbation_yuri_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/pose_mutual_masturbation_yuri.safetensors" "/content/stable-diffusion-webui/models/Lora/pose_mutual_masturbation_yuri.safetensors"
if Download_Sticky_Slime_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/sticky_slime_lycoris.safetensors" "/content/stable-diffusion-webui/models/Lora/sticky_slime_lycoris.safetensors"
if Download_Object_masturbation_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/object_masturbation.safetensors" "/content/stable-diffusion-webui/models/Lora/object_masturbation.safetensors"
if Download_Desk_Humping_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/desk_humping_masturbation_lycoris.safetensors" "/content/stable-diffusion-webui/models/Lora/desk_humping_masturbation_lycoris.safetensors"
if Download_masturbation_vibrator_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/masturbation_vibrator_hoshi119.safetensors" "/content/stable-diffusion-webui/models/Lora/masturbation_vibrator_hoshi119.safetensors"
if Download_Living_Clothes_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/living_clothes.safetensors" "/content/stable-diffusion-webui/models/Lora/living_clothes.safetensors"
if Download_yuri_tribadism_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/yuri_tribadism.safetensors" "/content/stable-diffusion-webui/models/Lora/yuri_tribadism.safetensors"
if Download_Anything_ColorMix:
  !cp -r "/content/gdrive/MyDrive/SD_Model/Anything5_ColorMix_fp16.safetensors" "/content/stable-diffusion-webui/models/Stable-diffusion/Anything5_ColorMix_fp16.safetensors"
if Download_Chromatic_aberration:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/Chromatic_aberration.safetensors" "/content/stable-diffusion-webui/models/Lora/Chromatic_aberration.safetensors"
if Download_Hassaku_Model_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/Hassaku_Hentai_model.safetensors" "/content/stable-diffusion-webui/models/Stable-diffusion/Hassaku_Hentai_model.safetensors"
if Download_BluePastel:
  !cp -r "/content/gdrive/MyDrive/SD_Model/BluePastel.safetensors" "/content/stable-diffusion-webui/models/Stable-diffusion/BluePastel.safetensors"
if Download_AuroraFantasty_V10:
  !cp -r "/content/gdrive/MyDrive/SD_Model/AuroraFantasty_V1.safetensors" /content/stable-diffusion-webui/models/Stable-diffusion/AuroraFantasty_V1.safetensors
if Download_Yuri_Kiss_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/yuri-kiss.safetensors" "/content/stable-diffusion-webui/models/Lora/yuri-kiss.safetensors"
if Download_pose_Mutual_masturbation0yuri0_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LyCORIS/yuri-mutual-masturbation.safetensors" "/content/stable-diffusion-webui/models/LyCORIS/yuri-mutual-masturbation.safetensors"
if Download_hoshi119_POV_yuri_cunnilingus_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/yuri-cunnilingus.safetensors" "/content/stable-diffusion-webui/models/Lora/yuri-cunnilingus.safetensors"
if Download_69_yuri_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/69-yuri.safetensors" "/content/stable-diffusion-webui/models/Lora/69-yuri.safetensors"
if Download_Naked_belt_outfit_of_ayachi_nene_cosplay_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/naked_belt_ayachi_nene.safetensors" "/content/stable-diffusion-webui/models/Lora/naked_belt_ayachi_nene.safetensors"
if Download_Bondage_Suspension_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/Bondage_suspension.safetensors" "/content/stable-diffusion-webui/models/Lora/Bondage_suspension.safetensors"
if Download_Milking_Machine_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/Milking_Machine.safetensors" "/content/stable-diffusion-webui/models/Lora/Milking_Machine.safetensors"
if Download_Kusanagi_nene:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/nene.safetensors" "/content/stable-diffusion-webui/models/Lora/nene.safetensors"
if Download_Tenma_saki:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/saki.safetensors" "/content/stable-diffusion-webui/models/Lora/saki.safetensors"
if Download_Akiyama_mizuki:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/mizuki.safetensors" "/content/stable-diffusion-webui/models/Lora/mizuki.safetensors"
if Download_Hoshino_ichika:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/ichika.safetensors" "/content/stable-diffusion-webui/models/Lora/ichikaaa.safetensors"
if Download_Azusawa_kohane:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/kohane.safetensors" "/content/stable-diffusion-webui/models/Lora/kohane.safetensors"
if Download_Yoisaki_kanade:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/kanade.safetensors" "/content/stable-diffusion-webui/models/Lora/kanade.safetensors"
if Download_Momoi_airi:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/airi.safetensors" "/content/stable-diffusion-webui/models/Lora/airi.safetensors"
if Download_Asahima_mafuyu:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/mafuyu.safetensors" "/content/stable-diffusion-webui/models/Lora/mafuyu.safetensors"
if Download_Hinomori_shizuku:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/shizuku.safetensors" "/content/stable-diffusion-webui/models/Lora/shizuku.safetensors"
if Download_Hinomori_shiho:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/Shiho.safetensors" "/content/stable-diffusion-webui/models/Lora/Shiho.safetensors"
if Download_Ootori_emu:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/emu.safetensors" "/content/stable-diffusion-webui/models/Lora/emu.safetensors"
if Download_Siraisi_ann:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/ann.safetensors" "/content/stable-diffusion-webui/models/Lora/ann.safetensors"
if Download_Mochizuki_honami:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/honami.safetensors" "/content/stable-diffusion-webui/models/Lora/honami.safetensors"
if Download_Kiritani_haruka:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/haruka.safetensors" "/content/stable-diffusion-webui/models/Lora/haruka.safetensors"
if Download_Hanasato_minori:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/minori.safetensors" "/content/stable-diffusion-webui/models/Lora/minori.safetensors"
if Download_Laby_Elsword:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/laby_elsword.safetensors" "/content/stable-diffusion-webui/models/Lora/laby_elsword.safetensors"
if Download_Shefii_Pricess_connect:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/shefii_prcn.safetensors" "/content/stable-diffusion-webui/models/Lora/shefii_prcn.safetensors"
if Download_Lowleg_clothing_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/Lowleg_clothing_panties.safetensors" "/content/stable-diffusion-webui/models/Lora/Lowleg_clothing_panties.safetensors"
if Download_Clothes_pull_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/pull_clothes_panties.safetensors" "/content/stable-diffusion-webui/models/Lora/pull_clothes_panties.safetensors"
if Download_BlueArchive_Sunaookami_Shiroko:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/sunaookami_shiroko.safetensors" "/content/stable-diffusion-webui/models/Lora/sunaookami_shiroko.safetensors"
if Download_Hatsune_miku:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/Hatsune_miku.safetensors" "/content/stable-diffusion-webui/models/Lora/Hatsune_miku.safetensors"
if Download_clothes_between_breasts_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/clothes_between_breasts.safetensors" "/content/stable-diffusion-webui/models/Lora/clothes_between_breasts.safetensors"
if Download_Genshin_impact_barbara:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/genshin_barbara.safetensors" "/content/stable-diffusion-webui/models/Lora/genshin_barbara.safetensors"
if Download_Pocky_kiss_side_view:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/pocky_game_sideview.safetensors" "/content/stable-diffusion-webui/models/Lora/pocky_game_sideview.safetensors"
if Download_AbyssOrangeMix2_DefMix140:
  !cp -r "/content/gdrive/MyDrive/SD_Model/AOM2-defmix1.1-40.safetensors" "/content/stable-diffusion-webui/models/Stable-diffusion/AOM2-defmix1.1-40.safetensors"
if Download_AbyssOrangeMix2_hard:
  !cp -r "/content/gdrive/MyDrive/SD_Model/AbyssOrangeMix2_hard.safetensors" "/content/stable-diffusion-webui/models/Stable-diffusion/AbyssOrangeMix2_hard.safetensors"
if Download_pjsekai_Miku:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/hatsune_miku_(project_sekai)_v1.safetensors" {lms}/hatsune_miku_project_sekai_v1.safetensors
if Download_Unknown_Sibuya_Rin:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/ShibuyaRinV2-03.safetensors" {lms}/ShibuyaRinV2.safetensors
if Download_Akiyama_Mizuki:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/AkiyamaMizukiV1.safetensors" {lms}/AkiyamaMizukiV1.safetensors
if Download_Anything_V5PrtRE:
  !cp -r "/content/gdrive/MyDrive/SD_Model/AnythingV5Ink_v5RE.ckpt" /content/stable-diffusion-webui/models/Stable-diffusion/Anything_V5-PrtRE.ckpt
if Download_Anything_V3:
  !cp -r "/content/gdrive/MyDrive/SD_Model/Anything-v3-full.safetensors" /content/stable-diffusion-webui/models/Stable-diffusion/Anything_V3-full.safetensors
if Download_POV_Across_Table:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/pov_across_table.safetensors" {lms}/pov_across_table.safetensors
if Download_penetration_Gesture:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/penetration_gesture.safetensors" {lms}/penetration_gesture.safetensors
if Download_ojou_sama_pose:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/ojou-sama_pose.safetensors" {lms}/ojou-sama_pose.safetensors
if Download_peace_sign:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/peace_sign.safetensors" {lms}/peace_sign-peace.safetensors
if Download_Slime_Girl_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/slime_girl.safetensors" {lms}/slime_girl.safetensors
if Download_Stained_Sheets_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/stained_sheets.safetensors" {lms}/stained_sheets.safetensors
if Download_lick_my_feet_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/lick_my_feet-feet-foot_focus.safetensors" {lms}/lick_my_feet-feet-foot_focus.safetensors
if Download_WHB_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/WHB.safetensors" {lms}/whb.safetensors
if Download_Bondage_outfit_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/bondage_outfit.safetensors" {lms}/bondage_outfit.safetensors
if Download_Suspension_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/suspension-spread_legs-rope-shibari.safetensors" {lms}/suspension-spread_legs-rope-shibari.safetensors
if Download_BDSM_Bandage_nsfw_warn:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/bdsm-bondage.safetensors" {lms}/bdsm-bondage.safetensors
if Download_masturbation_vibrator_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/vibrator.safetensors" {lms}/vibrator-vibrator_on_nipple-vibrator_under_clothes-etc.safetensors
if Download_solo_masturbation_handin_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/masturbating_handin.safetensors" {lms}/solo_masturbation_handin-hand_down_panties.safetensors
if Download_solo_masturbation_under_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/masturbating_under.safetensors" {lms}/solo_masturbation_under-masturbation_under_panties.safetensors
if Download_solo_masturbation_tables_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/masturbation_table.safetensors" {lms}/solo_masturbation_tables-table_sex.safetensors
if Download_solo_masturbation_normal_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/masturbation_normal.safetensors" {lms}/solo_masturbation_normal-masturbation.safetensors
if Download_yuri_kunnni_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/cunnilingus.safetensors" {lms}/yuri_cunnilingus.safetensors
if Download_yuri_pov_kunnni_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/pov_cun.safetensors" {lms}/yuri_pov_cun.safetensors
if Download_incoming_kiss:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/incoming_kiss.safetensors" {lms}/incoming_kiss.safetensors
if Download_cat_eyes:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/slit_pupils.safetensors" {lms}/slit_pupils.safetensors
if Download_Skin_Fang:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/skin_fang.safetensors" {lms}/skin_fang.safetensors
if Download_plastic_clothes_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/plastic_bag,swimsuit,.safetensors" {lms}/plastic_bag.safetensors
if Download_In_Water_Capsule:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/water_capsule.safetensors" {lms}/water_capsule.safetensors
if Download_In_Box:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/in_box.safetensors" {lms}/in_box.safetensors
if Download_In_Glass_Cup:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/glass_bottle.safetensors" {lms}/glass_bottle.safetensors
if Download_In_Glass_bottle_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/glass_jar.safetensors" {lms}/glass_jar.safetensors
if Download_Water_Torture_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/water_torture.safetensors" {lms}/water_torture.safetensors
if Download_Breast_Crimper_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/breast_crimper.safetensors" {lms}/breast_crimper.safetensors
if Download_BackArm_shibari_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/backarm_shibari.safetensors" {lms}/backarm_shibari.safetensors
if Download_Mechanical_Restraints_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/mechanical_restraints.safetensors" {lms}/mechanical_restraints.safetensors
if Download_Popsicle_Insertion_ntfs:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/popsicle_insertion.safetensors" {lms}/popsicle_insertion.safetensors
if Download_bubble_bra_ntfs:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/bubblebra.safetensors" {lms}/bubblebra.safetensors
if Download_hair_censor_ntfs:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/hair_censor.safetensors" {lms}/hair_censor.safetensors
if Download_bottomless_ntfs:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/bottomless.safetensors" {lms}/bottomless.safetensors
if Download_Pasties_ntfs:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/pasties.safetensors" {lms}/pasties.safetensors
if Download_Tentacles_ntfs:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/tentacles.safetensors" {lms}/tentacles.safetensors
if Download_reinohimo:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/reinohimo.safetensors" {lms}/reinohimo.safetensors
if Download_CN_ip2p:
  !cp -r "/content/gdrive/MyDrive/SD_Model/ControlNet/v11e_sd15_ip2p.pth" /content/stable-diffusion-webui/models/ControlNet/v11e_sd15_ip2p.pth
  !cp -r "/content/gdrive/MyDrive/SD_Model/ControlNet/v11e_sd15_ip2p.yaml" /content/stable-diffusion-webui/models/ControlNet/v11e_sd15_ip2p.yaml
if Download_CN_lineart_anime:
  !cp -r "/content/gdrive/MyDrive/SD_Model/ControlNet/v11p_sd15s2_lineart_anime.pth" /content/stable-diffusion-webui/models/ControlNet/v11p_sd15s2_lineart_anime.pth
  !cp -r "/content/gdrive/MyDrive/SD_Model/ControlNet/v11p_sd15s2_lineart_anime.yaml" /content/stable-diffusion-webui/models/ControlNet/v11p_sd15s2_lineart_anime.yaml
if Download_CN_openpose:
  !cp -r "/content/gdrive/MyDrive/SD_Model/ControlNet/v11p_sd15_openpose.pth" /content/stable-diffusion-webui/models/ControlNet/v11p_sd15_openpose.pth
  !cp -r "/content/gdrive/MyDrive/SD_Model/ControlNet/v11p_sd15_openpose.yaml" /content/stable-diffusion-webui/models/ControlNet/v11p_sd15_openpose.yaml
if Download_BlueArchive_Takanashi_Hosino:
  !cp -r  "/content/gdrive/MyDrive/SD_Model/LoRA/takanashi_hoshino.safetensors" {lms}/takanashi_hoshino.safetensors
if Download_incoming_hug:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/incoming_hug.safetensors" {lms}/incoming_hug.safetensors
if Download_Genshin_Klee:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/klee.safetensors" {lms}/klee.safetensors
if Download_BlueArchive_Saiba_Midori:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/midori1-000007.safetensors" {lms}/saiba_midori.safetensors
if Download_BlueArchive_Shizuyama_Mashiro:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/mashiro1-000007.safetensors" {lms}/shizuyama_mashiro.safetensors
if Download_WindLift_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/wind-lift.safetensors" {lms}/wind-lift.safetensors
if Download_Tentacle_clothes_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/tentacle_clothes.safetensors" {lms}/tentacle_clothes.safetensors
if Download_bodystocking_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/bodystocking.safetensors" {lms}/bodystocking.safetensors
if Download_Naked_Ribbon_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/NakedRibbon-dim=64-epoch=50.safetensors" {lms}/NakedRibbon.safetensors
if Download_Downblouse_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/EDB-000010.safetensors" {lms}/Extended_Downblouse.safetensors
if Download_Torn_Clothes_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/torn.safetensors" {lms}/torn.safetensors
if Download_cheerleader_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/cheerleaderOutfitV2.safetensors" {lms}/cheerleaderOutfitV2.safetensors
if Download_Bunnysuit_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/bunnysuit.safetensors" {lms}/bunnysuit.safetensors
if Download_CatTail_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/Lora/realtail_from_hehind.safetensors" {lms}/realtail_from_hehind.safetensors
if Download_school_swimsuit_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/Lora/scmz_blue_one-piece_swimsuit.safetensors" {lms}/scmz_blue_one-piece_swimsuit.safetensors
if Download_bunnygirl_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/Lora/bunnygirl.safetensors" {lms}/bunnygirl.safetensors
if Download_badhandv4:
  !cp -r "/content/gdrive/MyDrive/SD_Model/Textual-Inversion/badhandv4.pt" /content/stable-diffusion-webui/embeddings/badhandv4.pt
if Download_badhandv5:
  !cp -r "/content/gdrive/MyDrive/SD_Model/Textual-Inversion/badhandv5.pt" /content/stable-diffusion-webui/embeddings/badhandv5.pt

if Download_AbyssOrangeMix3:
  !cp -r "/content/gdrive/MyDrive/SD_Model/abyssorangemix3AOM3_aom3a1.safetensors" /content/stable-diffusion-webui/models/Stable-diffusion/abyssorangemix3AOM3_aom3a1.safetensors

if Download_EasyNegative:
  !cp -r "/content/gdrive/MyDrive/SD_Model/Textual-Inversion/EasyNegative.safetensors" /content/stable-diffusion-webui/embeddings/EasyNegative.safetensors

if Download_ichika_solo:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/ichika-solo Projectsekai (by. Onachinene in civitAI).safetensors" /content/stable-diffusion-webui/models/Lora/ichika.safetensors

if Download_luna_ichika:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/test.safetensors" /content/stable-diffusion-webui/models/Lora/luna_ichika.safetensors

if Download_ntfs_lunaichika:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/ichikaa.safetensors"  /content/stable-diffusion-webui/models/Lora/ntfs_lunaichika.safetensors

if Download_luna:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/ichika3.safetensors" /content/stable-diffusion-webui/models/Lora/global_ntfs_lunaichika.safetensors

if Download_YumekawaMix_A:
  !cp -r "/content/gdrive/MyDrive/SD_Model/1.4/YumekawaMix_A.safetensors" /content/stable-diffusion-webui/models/Stable-diffusion/YumekawaMix_A.safetensors
  !cp -r "/content/gdrive/MyDrive/SD_Model/1.4/YumekawaMix_X.vae.pt" "/content/stable-diffusion-webui/models/Stable-diffusion/YumekawaMix_A.vae.pt"
if Download_Masturbation_Boob_Fondling_and_Fingering_nsfw:
	!cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/masturbation-v1_satyam.safetensors" "/content/stable-diffusion-webui/models/Lora/masturbation_boob_fondling_and_fingering.safetensors"
if Download_Color:
	!cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/Vibrance-000005.safetensors" "/content/stable-diffusion-webui/models/Lora/color_000005.safetensors"
if Download_FromBelow_nsfw:
	!cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/frombelow-000004.safetensors" "/content/stable-diffusion-webui/models/Lora/frombelow-000004.safetensors"
if Download_TkskKurumi_SyokusyuV2_nsfw:
	!cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/触手v2.5_20.safetensors" "/content/stable-diffusion-webui/models/Lora/触手v2.5_20.safetensors"
if Download_Breasts_Heart_nsfw:
	!cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/boob_heart_80.safetensors" "/content/stable-diffusion-webui/models/Lora/boob_heart_80.safetensors"
if Download_In_Box_Girl_nsfw:
	!cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/NakedRibbon-dim=64-epoch=50.safetensors" "/content/stable-diffusion-webui/models/Lora/in_box_girl.safetensors"
if Download_Horosuke_Tentacles_nsfw:
	!cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/Horosuke‘s tentacle.safetensors" "/content/stable-diffusion-webui/models/Lora/Horosuke's_tentacle.safetensors"
if Download_ICE_Jelly_Tentacles_nsfw:
	!cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/big focking super tentacles.safetensors" "/content/stable-diffusion-webui/models/Lora/icejelly_tentacles.safetensors"
if Download_Perfect_Pussy_nsfw:
	!cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/pussy.safetensors" "/content/stable-diffusion-webui/models/Lora/perfect_pussy.safetensors"
if Download_Hoshi119_Tentacles_nsfw:
	!cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/qqq-tentacle_sex-v1.safetensors" "/content/stable-diffusion-webui/models/Lora/hoshi119_tentacles.safetensors"
if Download_YumekawaMix_B:
  !cp -r "/content/gdrive/MyDrive/SD_Model/1.4/YumekawaMix_B.safetensors" /content/stable-diffusion-webui/models/Stable-diffusion/YumekawaMix_B.safetensors
  !cp -r "/content/gdrive/MyDrive/SD_Model/1.4/YumekawaMix_X.vae.pt" "/content/stable-diffusion-webui/models/Stable-diffusion/YumekawaMix_B.vae.pt"

if Download_animeScreenshotLikeStyleMixLora_v10:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/animeScreenshotLikeStyleMixLora_v10.safetensors" /content/stable-diffusion-webui/models/Lora/animeScreenshotLikeStyleMixLora_v10.safetensors
if Download_Liquid_Clothes:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/liquid_cloth_dress.safetensors" "/content/stable-diffusion-webui/models/Lora/liquid_cloth_dress.safetensors"
if Download_Bondage_Outfit_Dominatrix_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/bondage_outfint_dominatrix.safetensors" "/content/stable-diffusion-webui/models/Lora/bondage_outfint_dominatrix.safetensors"
if Download_Miniskirt_plus:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/microskirt.safetensors" "/content/stable-diffusion-webui/models/Lora/microskirt.safetensors"
if Download_Naked_towel_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/naked_towel.safetensors" "/content/stable-diffusion-webui/models/Lora/naked_towel.safetensors"
if Download_Clothes_pull_446_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/clothes_pull_446.safetensors" "/content/stable-diffusion-webui/models/Lora/clothes_pull_446.safetensors"
if Download_Track_Uniform:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/track_uniform.safetensors" "/content/stable-diffusion-webui/models/Lora/track_uniform.safetensors"
if Download_Greek_Cloth:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/greek_clothes.safetensors" "/content/stable-diffusion-webui/models/Lora/greek_clothes.safetensors"
if Download_Plastic_Bag_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/plastic_bag.safetensors" "/content/stable-diffusion-webui/models/Lora/plastic_bag.safetensors"
if Download_Better_Naked_Bathrobe_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/better_naked_bathrobe.safetensors" "/content/stable-diffusion-webui/models/Lora/better_naked_bathrobe.safetensors"
if Download_Morrigan_Aensland_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/morrigan_aensland_vampire.safetensors" "/content/stable-diffusion-webui/models/Lora/morrigan_aensland_vampire.safetensors"
if Download_Dangerous_Beast_Cosplay:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/dangerous_beast_cosplay.safetensors" "/content/stable-diffusion-webui/models/Lora/dangerous_beast_cosplay.safetensors"
if Download_Onesie_Pajamas:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/animal_pajamas.safetensors" "/content/stable-diffusion-webui/models/Lora/animal_pajamas.safetensors"
if Download_Highleg_Sideless_Leotard_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/highleg_sideless_leotard_clothes_outfit.safetensors" "/content/stable-diffusion-webui/models/Lora/highleg_sideless_leotard_clothes_outfit.safetensors"
if Download_Cheerleader_BlueArchive:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/cheerleader_cosplay_bluearchive.safetensors" "/content/stable-diffusion-webui/models/Lora/cheerleader_cosplay_bluearchive.safetensors"
if Download_WHB_by_sevora_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/wooden_horse_sevora.safetensors" "/content/stable-diffusion-webui/models/Lora/wooden_horse_sevora.safetensors"
if Download_Yutori_Natsu_BlueArchive:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/yutori_natsu.safetensors" "/content/stable-diffusion-webui/models/Lora/yutori_natsu.safetensors"
if Download_Sumi_Serina_BlueArchive:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/sumi_serina.safetensors" "/content/stable-diffusion-webui/models/Lora/sumi_serina.safetensors"
if Download_neneka_prcn:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/neneka_prcn.safetensors" "/content/stable-diffusion-webui/models/Lora/neneka_prcn.safetensors"
if Download_Nahida_Genshin:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/nahida_genshin.safetensors" "/content/stable-diffusion-webui/models/Lora/nahida_genshin.safetensors"
if Download_WHB_by_psoft_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/whb_psoft.safetensors" "/content/stable-diffusion-webui/models/Lora/whb_psoft.safetensors"
if Download_A_Certain_Kind_of_Hospital_Gown:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/hospital_gown.safetensors" "/content/stable-diffusion-webui/models/Lora/hospital_gown.safetensors"
if Download_Akuma_Homura_BlackDress:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/homura_s_blackdress.safetensors" "/content/stable-diffusion-webui/models/Lora/homura_s_blackdress.safetensors"
if Download_Aisha_Landar_Elsword:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/aisha_landar.safetensors" "/content/stable-diffusion-webui/models/Lora/aisha_landar.safetensors"
if Download_MeinaModel_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/meinahentai_model_v2.1.safetensors" "/content/stable-diffusion-webui/models/Stable-diffusion/meinahentai_model_v2.1.safetensors"
if Download_Bondage_Amine:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/bondage_amine.safetensors" "/content/stable-diffusion-webui/models/Lora/bondage_amine.safetensors"
if Download_masusu_Breasts_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/masusu_breastandnipples.safetensors" "/content/stable-diffusion-webui/models/Lora/masusu_breastandnipples.safetensors"
if Download_Standing_cunniling_nsfw:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/stainding_cunnilingus.safetensors" "/content/stable-diffusion-webui/models/Lora/stainding_cunnilingus.safetensors"
if Download_LimeREmix_sweet_v2:
  !cp -r "/content/gdrive/MyDrive/SD_Model/limeremix_sweet_v2.safetensors" "/content/stable-diffusion-webui/models/Stable-diffusion/limeremix_sweet_v2.safetensors"
if Download_BlueArchive_Saiba_Momoi:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/saiba_momoi.safetensors" "/content/stable-diffusion-webui/models/Lora/saiba_momoi.safetensors"
if Download_Karyl_prcn:
  !cp -r "/content/gdrive/MyDrive/SD_Model/LoRA/karyl_v1.safetensors" "/content/stable-diffusion-webui/models/Lora/karyl_v1.safetensors"
"""

import os
from typing import Literal
from LGS.misc.jsonconfig import write_text

def extract_variable_from_if(line):
  compare = line.split("if")[1].strip()
  if compare.count(" ") >= 1 or compare.count(":") <= 0:
    print("\n[stderr]: Bad if-compare: ", compare)
    return None
  
  variable = compare.strip(":").strip()
  return variable

def convert_textual_from_texture(fp):
  old_fp = fp
  if "/SD_Model/Texture_Inversion".lower() in fp.lower():
    fp = fp.replace("Texture_Inversion", "Textual_Inversion")
  elif "/SD_Model/Textual-Inversion".lower() in fp.lower():
    fp = fp.replace("Textual-Inversion", "Textual_Inversion")

  onetime_command = ""
  
  if not old_fp == fp:
    onetime_command += f"\nos.rename('{old_fp}', '{fp}')"
    
  return fp, onetime_command
  
  
pathlike_ = {
}

ln = target_string.split("\n")
for index, line in enumerate(ln):
  line = line.strip()
  
  print("\nparsed ln", index+1, "..", end="")
  # parse command
  if line.startswith("if"):
    var = extract_variable_from_if(line)
    if var is None:
      continue
    pathlike_[var] = None
    
    print("done. with variable: ", var)
    continue
  
  if line.startswith("!cp"):
    compare = line.split("!cp")[1].strip()
    
    for c in compare.split(" "):
      c = c.strip('"').strip("'")
      if c.startswith("/content/gdrive/MyDrive/SD_Model"):
        break
      continue
    
    compare = c
    extracted_variable = extract_variable_from_if(ln[index-1])
    if extracted_variable is None:
      print("\n![stderr]: Unknown exception. extracted_variable is None.")
    
    pathlike_[extracted_variable] = compare

print(pathlike_)

onetime_cmd = []
variables = []
lora = {}
ti = {}
vae = {}
cnet = {}
ckpt = {}
unknown = {}

for index, (variable, fp) in enumerate(pathlike_.items()):
  mode:Literal["lora", "ckpt", "vae", "cnet", "ti"]
  if variable is not None:
    variables.append(variable)
  
  if "SD_Model/LoRA" in fp or "SD_Model/Lora" in fp or "SD_Model/lora" in fp:
    lora[variable] = fp
  elif "SD_Model/Texture_Inversion" in fp or "SD_Model/Textual-Inversion" in fp:
    fp, otc = convert_textual_from_texture(fp)
    onetime_cmd.append(otc)
    ti[variable] = fp
  elif "SD_Model/VAE" in fp or "SD_Model/VAE" in fp:
    vae[variable] = fp
  elif "SD_Model/ControlNet" in fp:
    cnet[variable] = fp
  else:
    if "SD_Model/1.4" in fp:
      unknown[variable] = fp
    
    else:
      ckpt[variable] = fp

notebook_string = ""
boolean_string = ""
ckpt_variables = []
lora_variables = []
ti_variables = []
cnet_variables = []
unknown_variables = []

notebook_string += "# Installing Stable-Diffusion Checkpoints..\nprint('Installing Stable-Diffusion Checkpoints..', end='')"
for v, f in ckpt.items():
  string = "if {v}: install_ckpt('{fn}')"
  fn = f.split("/")[-1].strip()
  notebook_string += f"\n{string.format(fn=fn, v=v)}"
  ckpt_variables.append(v)

notebook_string += "\nprint('done.')\n\n# Installing LoRA\nprint('Installing LoRA Models..', end='')"
for v, f in lora.items():
  string = "if {v}: install_lora('{fn}')"
  
  # 最後の / より後を取得
  fn = f.split("/")[-1].strip()
  if fn.endswith(".safetensors"):
    fn = fn.replace(".safetensors", "")
  
  notebook_string += f"\n{string.format(fn=fn, v=v)}"
  lora_variables.append(v)

notebook_string += "\nprint('.done')\n\n# Installing Textual Inversion\nprint('Installing Textual Inversion..', end='')"
for v, f in ti.items():
  string = "if {v}: install_ti('{fn}')"
  
  fn = f.split("/")[-1].strip()
  notebook_string += f"\n{string.format(v=v, fn=fn)}"
  ti_variables.append(v)

notebook_string += "\nprint('done.')\n\n# Installing ControlNet Models..\nprint('Installing ControlNet Models..', end='')"
for v, f in cnet.items():
  string = "if {v}: install_cnmodel('{fn}')"
  notebook_string += f"\n{string.format(v=v, fn=fn)}"
  cnet_variables.append(v)

notebook_string += "\nprint('done.')\n\n# Installing Other models..\nprint('Installing Other models..', end='')"
for v, f in unknown.items():
  if f.endswith(".vae"):
    continue
  
  string = f"if {v}: install_from_path('{f}')"
  notebook_string += f"\n{string}"
  unknown_variables.append(v)

onetime_command = "### onetime Command. please run onetime (for rename files.)"
for x in onetime_cmd:
  onetime_command += x


boolean_string += "#@markdown ## Install Stable-Diffusion Checkpoints"
ckpt_variable = sorted([x.replace("Download_", "") for x in ckpt_variables if x is not None])
lora_variable = sorted([x.replace("Download_", "") for x in lora_variables if x is not None])
ti_variable = sorted([x.replace("Download_", "") for x in ti_variables if x is not None])
cnet_variable = sorted([x.replace("Download_", "") for x in cnet_variables if x is not None])
unknown_variable = sorted([x.replace("Download_", "") for x in unknown_variables if x is not None])

for v in ckpt_variable:
  boolean_string += f'\nDownload_{v}'+' = False #@param {type: "boolean"}'#.format(v=v)

boolean_string += "\n#@markdown ## Install LoRA Models"
for v in lora_variable:
  boolean_string += f'\nDownload_{v}'+' = False #@param {type: "boolean"}'#.format(v=v)

boolean_string += "\n#@markdown ## Install Textual-Inversion"
for v in ti_variable:
  boolean_string += f'\nDownload_{v}'+' = False #@param {type: "boolean"}'#.format(v=v)

boolean_string += "\n#@markdown ## Install ControlNet Models"
for v in cnet_variable:
  boolean_string += f'\nDownload_{v}'+' = False #@param {type: "boolean"}'#.format(v=v)

boolean_string += "\n#@markdwon ### Install Other models"
for v in unknown_variable:
  boolean_string += f'\nDownload_{v}'+' = False #@param {type: "boolean"}'#.format(v=v)

print(locals())
write_text(f"""
          ### Install Model ###
          #
          #
{notebook_string}
          #
          # 
          ### Boolean String ###
          #
          #
{boolean_string}
          #
          #
          ### Onetime Command ###
          # 
          # 
{onetime_command}
          #
          #""", filepath="./notebookstyleupdater.py.out" ,overwrite=True)

print("\n\n\n\n\nDone.")
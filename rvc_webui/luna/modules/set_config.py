import json
import os
from pydantic import BaseModel, parse_file
from typing import List
from modules.shared import ROOT_DIR

class UITrainingConfig(BaseModel):
    config_version: str
    model_name: str
    dataset_path: str
    ignore_cache: bool
    normalize_audio: bool
    augment: bool
    augment_pretrain: bool
    
    lr: float
    lr_decay: float
    lr_decay_function: str # from ./luna/lib/train/lr_decay_object
    embed_channel: str # 256 or 768
    embedding_out_layer: str # 9 or 12
    embedder: str # hubert, hubert-base-jp, contentvec
    target_sr: str # 32k, 40k, 48k
    f0: bool
    fp16: bool
    batch_size: int
    epochs: int
    save_per_epoch: int
    infer_per_epoch: int
    pitch_extract_algorithm: str # dio, harvest, mangio-crepe, crepe
    model_version: str # v1, v2
    cpu_count: int
    save_wav_with_cp: bool
    recursive: bool
    pretrain_g: str
    pretrain_d: str
    pretrain_g_al: str
    speaker_info: str
    train_index: bool
    reduce_index: bool
    max_index: int
    
    auto_close: bool
    terminate_session: bool
    remove_dataset: bool
    full_parameter: bool
    model_output: str
    
    @classmethod
    def parse_file(cls, 
            config_path: str):
        # ファイルを読み込み、JSONデータをPydanticモデルに変換
        with open(config_path, 'r', encoding='utf-8') as config_file:
            config_data = json.load(config_file)
        return cls(**config_data)
## Define Example
# UITrainingConfig.parse_file(os.path.join(ROOT_DIR, "luna", "configs", "ui", "training"))

# define
def update():
    return UITrainingConfig.parse_file(os.path.join(ROOT_DIR, "luna", "configs", "ui", "training"))
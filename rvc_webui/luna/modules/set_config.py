from pydantic import BaseModel, parse_file
from typing import *
import json

class UITrainingConfig(BaseModel):
    config_version: str
    model_name: str
    dataset_path: str
        
        
    @classmethod
    def parse_file(cls, config_path):
        # ファイルを読み込み、JSONデータをPydanticモデルに変換
        with open(config_path, 'r') as config_file:
            config_data = json.load(config_file)
        return cls(**config_data)
      
## Define Example
# UITrainingConfig.parse_file(os.path.join(ROOT_DIR, "luna", "configs", "ui", "training"))
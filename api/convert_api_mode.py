"""
### lunapy API Mode

`Scripts/{name}/convert_api.py` が存在する全てのモジュールの API からの呼び出しをサポートする

使用方法: 
```python
from luna_py.api.convert_api_mode import api_mode

# モジュール: JPG2PNG Converter を呼び出す
lunapy_image_format_converter:lunapyScripts = api_mode("jpg2png converter")
```
"""
class lunapyScripts: initial_ = None
import overview
from PIL import Image
import torch
import torchvision.transforms as transforms
from torchvision.datasets import MNIST

transform = transforms.Compose([
    transforms.ToTensor(),   # データをテンソルに変換
    transforms.Normalize((0.5,), (0.5,))  # 正規化
])

new_image = Image.open('path_to_image.jpg')  # 画像の読み込み
new_image = transform(new_image)  # 前処理

# モデルを評価モードに設定
model = overview.SimpleCNN()

# モデルの読み込み
model.load_state_dict(torch.load('./models/model.pth'))


model.eval()

# 予測
with torch.no_grad():
    output = model(new_image.unsqueeze(0))  # バッチ次元を追加して予測

# 確率スコアからクラスを予測
predicted_class = torch.argmax(output, dim=1).item()

print(f"Predicted class: {predicted_class}")
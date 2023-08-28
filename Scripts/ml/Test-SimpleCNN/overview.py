import torch
import torch.nn as nn
from tqdm import tqdm
from os import makedirs as mkdir
from torch.utils.data import DataLoader
import torch.optim as optim
import torchvision.transforms as transforms
from torchvision.datasets import MNIST

# モデルの定義
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, padding=1)
        # nn.Conv2d 畳み込み層の定義 
        # 入力、出力チャンネルを定義、フィルタのサイズ (kernel_size) とぜろぱっディング (padding)を定義
        self.relu = nn.ReLU()
        # ReLuは活性化関数で、負の値を0にクリップして非線形性を導入する
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        # MaxPool2d 最大プーリング値の定義
        self.fc = nn.Linear(16 * 14 * 14, 10)  # MNISTデータセット用に設定
        # Linear 結合層の定義
        # 16 * 14 * 14 の特徴を 10 次元に出力する
        
    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x

# モデルのインスタンス化
print("Model Building..")
model = SimpleCNN()
print("Done!")

# 損失関数とオプティマイザの定義
criterion = nn.CrossEntropyLoss() # CrossEntropy を使用した損失関数の定義
# Adam Optimizerの定義、Learning Rateの定義
optimizer = optim.Adam(model.parameters(), lr=0.001)

# データセットの前処理

# データの前処理を定義
print("Dataset Preproccessing..")
transform = transforms.Compose([
    transforms.ToTensor(),   # データをテンソルに変換
    transforms.Normalize((0.5,), (0.5,))  # 正規化
])

# MNISTデータセットの読み込み
train_dataset = MNIST(root='./data', train=True, transform=transform, download=True)
train_loader = DataLoader(dataset=train_dataset, batch_size=2, shuffle=True)
# root: データセットを保存するディレクトリのパスを指定します。ここでは ./data と指定されており、MNISTデータセットがこのディレクトリ内に保存されます。
# transform: データの前処理を行うための変換パイプラインを指定します。ここでは transform 変数に前処理パイプラインを指定しています。
# download: データセットが存在しない場合に、自動的にダウンロードするかどうかを指定します。True にすることで、データセットが存在しない場合にダウンロードが行われます。
print("Done!")

# 学習ループ
print("Model Training Starting..")
for epoch in tqdm(range(20)):
    # モデルをトレーニングモードに設定
    model.train()
    
    for inputs, labels in train_loader:  # ミニバッチごとにデータを取得
        optimizer.zero_grad()  # 勾配を初期化
        
        outputs = model(inputs)  # モデルの出力を計算
        loss = criterion(outputs, labels)  # 損失を計算
        loss.backward()  # 勾配を計算
        
        optimizer.step()  # パラメータを更新
        
    print(f'\nEpoch ({epoch+1}/20).  loss_d: {loss.item():.10f}')
  
print("Done!")

print("Model Saving..")
mkdir("./models", exist_ok=True)
torch.save(model.state_dict(), './models/model.pth')
print("Done!")

print("All Process Ended.")
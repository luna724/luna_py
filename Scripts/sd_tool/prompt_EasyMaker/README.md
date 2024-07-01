## JA
SD-PEM刷新 `v3 -> v4`

SDPEM は SDPDB との互換性のために大幅な変更を加えられ、
SDPDBへのAPIを提供しつつ SDPEM の UI も起動可能なスクリプトになります
現在 UIの完全起動は [`launch_v3.bat`] にてサポートされています。
また、新機能へのアクセスは `v4β.bat` からの起動で可能です。

- [v4の変更内容に関するログ](Changelogs.md)
- [v4のTODO](TODO.md)


## SD-PEM / Stable-Diffusion Prompt Easy Maker v4

### 概要
テキストおよび変数のセットを json で保存し、それらのビルドを簡潔に行うためのもの

### 実行方法 
#### (SD-PEM v3)
1. `launch_v3.bat` を起動
2. `localhost:7860` に接続し、操作を行う

#### (SD-PEM v4)
1. `v4β.bat` を起動
2. `localhost:7859` に接続し、操作を行う

#### (SD-PDB v1r)
0. `AUTOMATIC1111/Stable-Diffusion WebUI` を導入する
1. https://github.com/luna724/sdpdb から SD-PDBを取得
2. `extensions/` に導入
3. システムに基づくファイルにより、SD-WebUIを実行
4. タブ `SDPDB` に移動し、操作を行う

### config.json 説明
あとでついか

### 他モジュールとの連携機能
- [SDPDB](https://github.com/luna724/sdpdb) `Private:β1-4`
  - APIを提供。 SD-PEM は SD-PDB では必須要素となっている

- [GenDataSaver](https://github.com/luna724/sd_gendatasaver) `Private:R1-01+`
  - PEM形式でのデータ一時保管のサポート
  - その他 PEM に依存する機能多数

- [ShareYourImage!](https://github.com/luna724/sd_syi) `Private:β1-2`
  - 「PEM形式 json の送信」機能のサポート

- [SomeTweaks](https://github.com/luna724) `Planning`
  - SDPDB の出力を一括で移動する機能の提供？

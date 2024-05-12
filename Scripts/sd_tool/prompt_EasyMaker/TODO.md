`WIP > 1`

1. revamp API
### API の詳細
関数をすべて
PDBが定義可能な変数をすべて __init__ で定義するクラスに変更

2. Optimize error
### 詳細
現在エラーはすべて raise にて管理されている
それらを特別関数の呼び出しを通じて gr.Error や RuntimeError (pdb=前者、pem=後者) で呼び出し可能にする
あとついでにエラーハンドリングがしやすくなる
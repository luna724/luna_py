# tiny tiny scripts
微かな行為を自動化するために作られたスクリプトたち
起動方法はすべて共通で `python [script_name].py` で実行可能 (一部venv環境を要求)
```bat
@rem venvへのアクセス方法

call ..\..\./.venv/scripts/activate
python {script_name}.py
```

| script名 | 概要 | venvが必要がどうか |
| --- | --- | --- |
| notebookstyleupdater | Colab notebook のモデルリストを新しいコードに適応させるためのもの | 必 |
| rvcvccmm | R-VCのコンフィグマネージャーのコードを自動生成するもの | 必 |
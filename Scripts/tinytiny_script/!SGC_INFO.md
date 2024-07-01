## Simple Graph Creator Syntax Information
 <center>Simple Graph Creator 記述ルール説明</center>

例:
```txt
x_axis\&y_axis
Example Graph
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
!?simple_graph_creator.py.png
```

値:
```txt 
   !SGC_input.txt
{x_label}\&{y_label}
{info_text}
{graph_values}
!{output_path}
```

1. {x_label}\\&{y_label}
これらは x,y の値の単位を現す位置に表示され、`\&` で分割されます。
改行は含めません
最初に ! は使用できません。

2. {info_text}
これは グラフの下に配置される説明文です。
改行は含めません
最初に ! は使用できません。

3. {graph_values}
これはグラフの値のリストです。
このリストは python の Syntax に沿っている必要があり、list(graph_values) で処理されます。
改行を含むことができます。
全ての値は int/float である必要があります

```py
# 処理方法詳細
def convert_graph_values(v:str) -> List[int]:
  v = v.strip("[","]")
  l = []

  for x in v.split(","):
    x = x.strip("\n").strip()
    
    if x.isdigit():
      l.append(int(x))
    else:
      l.append(float(x))
  
  return l

graph_values = "[0, 2.4, 8, 42.1, 1, 5.75, -2]"
convert_graph_values(graph_values)
```

4. {output_path}
[Optional] 任意
グラフ画像の出力パスを示します
ディレクトリが存在しない場合、エラーを返します

`\n!` で graph_values との分割を行います。
相対パスにする場合は `?path..` のように `?` をヘッダーにする必要があります
相対パスの場合、`tinytiny_script/` からの相対パスを示します
# Markdown Preview Enhancedの利用例

## GitHubのnote記法を導入

`parser.js`と`style.less`を編集するとレンダリングがされる。

以下のスクリプトを実行すると`github_parser.js`と`github_style.less`の内容が`parser.js`と`style.less`へ転記される。（2025/05時点で動作確認済み）

- `/home/jovyan/work/src/Sample/Program/Python_Script/Markdown_Preview_Enhanced/parser/change_parser.py`
- `/home/jovyan/work/src/Sample/Program/Python_Script/Markdown_Preview_Enhanced/css/change_style.py`

以下が使用例となる。

- `NOTE`

> [!NOTE]  
> Highlights information that users should take into account, even when skimming.

- `TIP`

> [!TIP]
> Optional information to help a user be more successful.

- `IMPORTANT`

> [!IMPORTANT]  
> Crucial information necessary for users to succeed.

- `WARNING`

> [!WARNING]  
> Critical content demanding immediate user attention due to potential risks.

- `CAUTION`

> [!CAUTION]
> Negative potential consequences of an action.

## 数式の挿入

`$` または `\(` と `\)` で囲うとインライン数式、
`$$` または `\[`と `\]` で囲うとディスプレイ数式が書ける。

### インライン数式

$e^{i\pi} + 1 = 0$のように書ける。

### ディスプレイ数式

$$
\mathbf{A} \cdot ( \mathbf{B} \times \mathbf{C} ) = \left| \begin{array}{ccc} A_1 & A_2 & A_3 \\ B_1 & B_2 & B_3 \\ C_1 & C_2 & C_3 \end{array} \right| = \varepsilon_{ijk} A_i B_j C_k \tag{1.1}
$$

のように書ける。

## コードブロック

Markdownでコードブロックを挿入するには、バッククォート（\`）を3つ連続で入力し、その後に言語名（例:python）を記述する。  
コードの記述が終わったら、再度バッククォート3つで閉じる。

例：

```python
import sys
print(sys.version)
```

### 行数の表示

コードブロック内で行番号を表示したい場合は、  
バッククォートの後に `{class="line-numbers"}` を付与する。

```python {class="line-numbers"}
import sys
print(sys.version)
```

### コードチャンク

Markdown Preview Enhancedではコードを実行しレンダリングすることができる。
これを行うには、バッククォートの後に `{cmd}` を付与する。

レンダリングするには、`{hide}`オプションを付与していない場合は、
`Preview`側のコードが表示されている部分へマウスをホバーした際に表示される`ALL`または`▶`をクリックするとコードが実行されて結果が表示される。

- `ALL`はすべてのコードブロックが実行される。
- `▶`は単一のコードブロックが実行される。

`{hide}`オプションを付与している場合は、`ctrl`+`Shift`+`Enter`を`.md`ファイル側で行うとすべてレンダリングされる。

> [!NOTE]
> `settings.json`にて`"markdown-preview-enhanced.enableScriptExecution": true`とする必要がある。

```python {cmd class="line-numbers"}
import sys
print(sys.version)
```

#### matplotlib

matplotlibのグラフを表示するには、`{matplotlib}` を付与する。

```python {cmd matplotlib class="line-numbers"}
import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5])
plt.show()
```

作図結果のみを表示し、コードを表示したくない場合は、`{hide}`を付与する。

```python {cmd matplotlib hide}
import matplotlib.pyplot as plt
plt.plot([5,4,3,2,1])
plt.show()
```

#### LaTeX

複雑な数式やLaTeXの`tikz`関連の高度な作図ツールを利用したい場合、LaTeXコードチャンクで対応できる。
`{latex_zoom=300%}`がないとエラーとなった。（2025/05時点）

- Hello world!という文字列を表示

```latex {cmd=true, latex_zoom=300%}
\documentclass{standalone}
\begin{document}
  Hello world!
\end{document}
```

- `tkiz`

```latex {cmd=true, latex_zoom=300%}
\documentclass{standalone}
\usepackage{tikz}
\begin{document}
  \begin{tikzpicture}[samples=100]
    \draw[->,>=stealth,semithick] (-0.3,0)--(2,0) node[right]{$x$};
    \draw[->,>=stealth,semithick] (0,-0.3)--(0,3) node[above]{$y$};
    \draw (0,0) node[below left]{O};

    % 過剰和を赤色、不足和を青色で示す
    \foreach \x in {0.0, 0.2, ..., 1.6}
      \filldraw[fill=red!20] (\x,0) rectangle (\x+0.2,{max(\x*\x,(\x+0.2)*(\x+0.2))});
      
    \foreach \x in {0.0, 0.2, ..., 1.6}
      \filldraw[fill=blue!20] (\x,0) rectangle (\x+0.2,{min(\x*\x,(\x+0.2)*(\x+0.2))});

    \draw[domain=-0.3:1.85] plot(\x,{\x*\x});
  \end{tikzpicture}
\end{document}
```

- `circuitikz`

```latex {cmd=true, latex_zoom=300%}
\documentclass{standalone}
\usepackage{tikz}
\usepackage{circuitikz}
\begin{document}
  \begin{circuitikz}[american currents]
    \draw (0,0)
      to[sV=$E$] (0,2)
      to[short] (2,2)
      to[european resistor=$R$] (2,0)
      to[short] (0,0);
    \draw (2,2)
      to[short] (4,2)
      to[L=$L$] (4,0)
      to[short] (2,0);
    \draw (4,2)
      to[short] (6,2)
      to[C=$C$] (6,0)
      to[short] (4,0);
  \end{circuitikz}
\end{document}
```

## import文によるファイルのインポート

`@import "file_path"`により、有名な形式のファイルをそのままインポートできるというすごいやつ。インポートできるファイルの種類は公式Docs参照。

- `csv`ファイルを表としてレンダリング

@import "table.csv"

## 参考

### 公式Docs

<https://shd101wyy.github.io/markdown-preview-enhanced/#/ja-jp/>
<https://shd101wyy.github.io/markdown-preview-enhanced/#/ja-jp/code-chunk>
<https://shd101wyy.github.io/markdown-preview-enhanced/#/file-imports>

### 記事

<https://qiita.com/take_me/items/5ff5304b58d9feec21df>
<https://qiita.com/MrMocchy/items/404fab9031a9296ab118>
<https://atatat.hatenablog.com/entry/cloud_latex31_circuitikz>

<https://qiita.com/Yarakashi_Kikohshi/items/407f85ba2835d945dd5b#fn-editor>
<https://trap.jp/post/1791/>

### GitHub.css

<https://qiita.com/__mick/items/c80fab6c185a41882880>
<https://raw.githubusercontent.com/sindresorhus/github-markdown-css/gh-pages/github-markdown.css>

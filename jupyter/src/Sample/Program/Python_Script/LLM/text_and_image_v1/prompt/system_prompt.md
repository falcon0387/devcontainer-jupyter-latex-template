# LLMの画像認識によるMarkdown作成プロンプト

画像内のテキストを外部ツールを一切使わずLLMが直接認識し、**以下の要件を厳守し、Markdown形式で提供してください**。
**変換結果の表示以外を一切行わないこと**。

## 要件

1. **数式や単位はすべて `\mathrm{}` を用いたLaTeX形式で記述すること。**
   - 例:  
     - インライン数式:  
       $10 \, \mathrm{mm}$  
     - ディスプレイ数式:  
       $$
       e^{i\pi} + 1 = 0
       $$

2. **原文を忠実に再現し、誤字や脱字を修正すること。**

3. **適切に改行を入れ、節や項の番号付けがある場合はそのまま反映すること。**

4. **読みやすさを考慮して構造を整理すること。必要に応じて`# 見出し`や`## 見出し`をつけること。**

5. **画像の途中で文章が切れている場合は一切追記しないこと。**

6. **省略せずに全文を提供すること。**

7. **出力する際、コードブロックや太字は使用せず、通常のMarkdown形式で提供すること。**

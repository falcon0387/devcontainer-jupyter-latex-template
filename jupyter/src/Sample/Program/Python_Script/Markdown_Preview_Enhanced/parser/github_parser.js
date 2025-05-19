({
  onWillParseMarkdown: async function (markdown) {
    // GitHub風のアラート記法を処理
    // > [!NOTE] の形式を検出して変換
    markdown = markdown.replace(/^>\s*\[!NOTE\]\s*\n((?:^>.*\n?)*)/gm, (match, content) => {
      const cleanContent = content.replace(/^>/gm, '').trim();
      return `<alert class="alert-note">
<alert-title>Note</alert-title>
${cleanContent}
</alert>\n`;
    });

    markdown = markdown.replace(/^>\s*\[!IMPORTANT\]\s*\n((?:^>.*\n?)*)/gm, (match, content) => {
      const cleanContent = content.replace(/^>/gm, '').trim();
      return `<alert class="alert-important">
<alert-title>Important</alert-title>
${cleanContent}
</alert>\n`;
    });

    markdown = markdown.replace(/^>\s*\[!WARNING\]\s*\n((?:^>.*\n?)*)/gm, (match, content) => {
      const cleanContent = content.replace(/^>/gm, '').trim();
      return `<alert class="alert-warning">
<alert-title>Warning</alert-title>
${cleanContent}
</alert>\n`;
    });

    markdown = markdown.replace(/^>\s*\[!TIP\]\s*\n((?:^>.*\n?)*)/gm, (match, content) => {
      const cleanContent = content.replace(/^>/gm, '').trim();
      return `<alert class="alert-tip">
<alert-title>Tip</alert-title>
${cleanContent}
</alert>\n`;
    });

    markdown = markdown.replace(/^>\s*\[!CAUTION\]\s*\n((?:^>.*\n?)*)/gm, (match, content) => {
      const cleanContent = content.replace(/^>/gm, '').trim();
      return `<alert class="alert-caution">
<alert-title>Caution</alert-title>
${cleanContent}
</alert>\n`;
    });

    // より簡潔な記法も対応（タイトルなし）
    markdown = markdown.replace(/^>\s*\[!(\w+)\]\s*\n((?:^>.*\n?)*)/gm, (match, type, content) => {
      const alertType = type.toLowerCase();
      const cleanContent = content.replace(/^>/gm, '').trim();
      const title = type.charAt(0).toUpperCase() + type.slice(1).toLowerCase();
      
      return `<alert class="alert-${alertType}">
<alert-title>${title}</alert-title>
${cleanContent}
</alert>\n`;
    });

    return markdown;
  },

  onDidParseMarkdown: async function (html) {
    return html;
  },

  onWillTransformMarkdown: async function (markdown) {
    return markdown;
  },

  onDidTransformMarkdown: async function (markdown) {
    return markdown;
  },

  processWikiLink: function ({ text, link }) {
    return {
      text,
      link: link ? link : text.endsWith(".md") ? text : `${text}.md`,
    };
  },
});
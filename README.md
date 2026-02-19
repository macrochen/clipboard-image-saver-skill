# Clipboard Image Saver Skill

这是一个简单的 Gemini CLI 技能，用于快速将剪贴板中的图像保存为本地文件。

## 功能

- 检测剪贴板内容。
- 如果是图片，则保存至 `~/Downloads`。
- 文件名格式：`clipboard_YYYYMMDD_HHMMSS.png`。

## 安装依赖

该技能使用项目根目录 `.venv` 中的 `pillow` 库。

## 使用方法

直接对 Gemini 说：
- "帮我把剪贴板的图片存一下"
- "Save clipboard image"

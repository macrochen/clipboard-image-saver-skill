---
name: clipboard-image-saver-skill
description: "将剪贴板中的图片保存到本地下载目录。支持时间戳命名，适用于快速保存截图或网页复制的图片。"
---

# Clipboard Image Saver Skill

此技能可以将剪贴板中的图片保存到系统的 Downloads 目录下，并以时间戳命名。

## 默认输出位置

保存结果默认位于：

```text
~/Downloads/clipboard_YYYYMMDD_HHMMSS.png
```

如果剪贴板中是多个图片文件路径，则会保存为：

```text
~/Downloads/clipboard_YYYYMMDD_HHMMSS_<原文件名>
```

## 工具定义

### save_clipboard_image

将剪贴板中的图片内容保存到 `~/Downloads` 目录下。

#### 参数

此工具不需要任何参数。

## 指令

- 当用户要求“保存剪贴板图片”、“下载剪贴板里的图”或类似指令时，调用 `save_clipboard_image`。
- 如果剪贴板中不是图片，脚本会自动忽略并给出提示。

## 运行环境

- 该技能依赖于项目根目录下的 `.venv` 虚拟环境。
- 需要 `pillow` 库支持。

## 实现细节

调用方式：
```bash
source .venv/bin/activate && python ~/.agents/skills/clipboard-image-saver-skill/save_image.py
```

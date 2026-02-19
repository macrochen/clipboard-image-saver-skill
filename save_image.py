import os
import sys
from datetime import datetime
from pathlib import Path
from PIL import ImageGrab, Image

def save_clipboard_image():
    # 检查剪贴板内容
    try:
        img_content = ImageGrab.grabclipboard()
    except Exception as e:
        print(f"读取剪贴板失败: {e}")
        return

    if img_content is None:
        print("剪贴板中没有图片内容。")
        return

    downloads_path = Path.home() / "Downloads"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # 情况 1: 剪贴板里是直接的图片数据 (Image 对象)
    if isinstance(img_content, Image.Image):
        filename = f"clipboard_{timestamp}.png"
        save_path = downloads_path / filename
        try:
            img_content.save(save_path, "PNG")
            print(f"图片已成功保存至: {save_path}")
        except Exception as e:
            print(f"保存图片失败: {e}")
            
    # 情况 2: 剪贴板里是文件路径列表 (例如在 Finder 中复制了图片文件)
    elif isinstance(img_content, list):
        image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp'}
        saved_count = 0
        for item in img_content:
            file_path = Path(item)
            if file_path.suffix.lower() in image_extensions:
                # 如果是文件，我们就复制一份到下载目录，或者重新保存
                filename = f"clipboard_{timestamp}_{file_path.name}"
                save_path = downloads_path / filename
                try:
                    with Image.open(file_path) as img:
                        img.save(save_path)
                    print(f"已从文件来源保存图片至: {save_path}")
                    saved_count += 1
                except Exception as e:
                    print(f"处理文件 {file_path.name} 失败: {e}")
        if saved_count == 0:
            print("剪贴板中的文件不是图片。")
    else:
        print("剪贴板内容不是有效的图片。")

if __name__ == "__main__":
    save_clipboard_image()

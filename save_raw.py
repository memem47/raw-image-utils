# save_raw.py

from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

def create_pattern_image(width, height):
    """横縞パターン画像をPIL Imageで生成（グレースケール）"""
    arr = np.tile(np.linspace(0, 255, width, dtype=np.uint8), (height, 1))
    return Image.fromarray(arr, mode="L")

def draw_centered_text(image: Image.Image, text: str) -> Image.Image:
    """中央にテキストを描画する（白抜きの黒文字）"""
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("arial.ttf", size=image.height // 6)
    except IOError:
        font = ImageFont.load_default()

    text_size = draw.textbbox((0, 0), text, font=font)
    text_width = text_size[2] - text_size[0]
    text_height = text_size[3] - text_size[1]

    position = ((image.width - text_width) // 2, (image.height - text_height) // 2)

    # 白抜き影＋黒文字（視認性UP）
    draw.text((position[0] + 2, position[1] + 2), text, fill=255, font=font)
    draw.text(position, text, fill=0, font=font)

    return image

def save_sample_raw_images():
    width, height = 256, 256

    # --- 8bit image ---
    img_8bit = create_pattern_image(width, height)
    img_8bit = draw_centered_text(img_8bit, "8bit")
    arr_8bit = np.array(img_8bit, dtype=np.uint8)
    path_8bit_raw = f"sample_{width}x{height}_8bit.raw"
    path_8bit_png = f"sample_{width}x{height}_8bit.png"
    arr_8bit.tofile(path_8bit_raw)
    img_8bit.save(path_8bit_png)

    # --- 16bit image ---
    img_16bit = create_pattern_image(width, height)
    img_16bit = draw_centered_text(img_16bit, "16bit")
    arr_16bit_uint8 = np.array(img_16bit, dtype=np.uint8)
    arr_16bit = arr_16bit_uint8.astype(np.uint16) * 256
    path_16bit_raw = f"sample_{width}x{height}_16bit.raw"
    path_16bit_png = f"sample_{width}x{height}_16bit.png"
    arr_16bit.tofile(path_16bit_raw)
    img_16bit.save(path_16bit_png)

    return {
        "width": width,
        "height": height,
        "path_8bit": path_8bit_raw,
        "path_16bit": path_16bit_raw,
        "path_8bit_png": path_8bit_png,
        "path_16bit_png": path_16bit_png,
    }

# 実行時のみファイル作成
if __name__ == "__main__":
    info = save_sample_raw_images()
    print("Saved files:")
    print(info)

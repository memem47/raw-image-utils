# test_view_raw.py

import numpy as np
import matplotlib.pyplot as plt
import save_raw  # 同じディレクトリにある必要あり

def load_and_show_raw(path, width, height, dtype, title):
    with open(path, "rb") as f:
        arr = np.frombuffer(f.read(), dtype=dtype).reshape((height, width))
    plt.imshow(arr, cmap="gray")
    plt.title(f"{title} ({dtype.__name__})")
    plt.axis("off")
    plt.show()

def main():
    # 8bitと16bit RAW画像を作成
    info = save_raw.save_sample_raw_images()

    # 読み込み・表示
    load_and_show_raw(info["path_8bit"], info["width"], info["height"], np.uint8, "8bit RAW")
    load_and_show_raw(info["path_16bit"], info["width"], info["height"], np.uint16, "16bit RAW")

if __name__ == "__main__":
    main()

import face_recognition
import cv2
import numpy as np
import sys
import os
from PIL import Image, ImageDraw, ImageFont
from pilmoji import Pilmoji

def add_emoji_to_image(image: cv2.typing.MatLike, face_location, emoji):
    top, right, bottom, left = face_location
    face_width = right - left
    face_height = bottom - top

    # 创建一个和人脸同样大小的透明图像
    emoji_image = Image.new('RGBA', (face_width, face_height), (0, 0, 0, 0))
    pilmoji = Pilmoji(emoji_image)

    # 计算 Emoji 字体大小
    font_size = max(face_width, face_height)
    font = ImageFont.truetype("Arial.ttf", font_size)

    # 使用 PILmoji 在透明图像上绘制 Emoji
    pilmoji.text((0, 0), emoji, font=font, fill=(255, 255, 255, 255))

    # 将 PIL 图像转换为 OpenCV 图像
    emoji_image_cv = cv2.cvtColor(np.array(emoji_image), cv2.COLOR_RGBA2BGRA)

    # 将 Emoji 图像叠加到原始图像的人脸位置
    # emoji_image.show()
    # print(face_location)
    emoji_channels = cv2.split(emoji_image_cv)
    emoji_bgr = cv2.merge(emoji_channels[:3])  # 获取 BGR 通道
    emoji_alpha = emoji_channels[3]            # 获取 Alpha 通道

    # 在原始图像上创建 ROI（感兴趣区域）
    roi = image[top:bottom, left:right]

    # 将 Emoji 应用于 ROI
    img_bg = cv2.bitwise_and(roi, roi, mask=cv2.bitwise_not(emoji_alpha))
    img_fg = cv2.bitwise_and(emoji_bgr, emoji_bgr, mask=emoji_alpha)

    # 合并 FG 和 BG
    dst = cv2.add(img_bg, img_fg)
    image[top:bottom, left:right] = dst


def detect_and_add_emoji(image_path, emojis):
    # 使用 face_recognition 加载图像（以 RGB 格式）
    image = face_recognition.load_image_file(image_path)
  
    face_locations = face_recognition.face_locations(image)

    # 将图像从 RGB 转换为 BGR
    image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # 在每个检测到的人脸上添加 Emoji
    for face_location in face_locations:
        emoji = np.random.choice(emojis)
        add_emoji_to_image(image_bgr, face_location, emoji)

    # 构建输出文件路径
    base_path, ext = os.path.splitext(image_path)
    output_path = base_path + "_emoji" + ext
    cv2.imwrite(output_path, image_bgr)
    print(f"Image with emojis saved as {output_path}")

if __name__ == "__main__":
    emojis = "😀 😃 😄 😁 😆 😅 😂 🤣 😊 😇 😉 😌 😍 😘 😗 😙 😚 😋 😛 😝 😜 🤪 🤨 🧐 🤓 😎 🤩 🥳 😏 😒 😞 😔 😟 😕 🙁 😣 😖 😫 😩 🥺 😢 😭 😤 😠 😡 🤬 🤯 😳 🥵 🥶 😱 😨 😰 😥 😓 🤗 🤔 🤭 🤫 🤥 😶 😐 😑 😬 🙄 😯 😦 😧 😮 😲 🥱 😴 🤤 😪 😵 🤐 🥴 🤧 😷 🤒 🤕 🤑 🤠".split()
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        detect_and_add_emoji(image_path, emojis)
    else:
        print("Please provide an image path.")

import face_recognition
import cv2
import numpy as np
import sys
import os
from PIL import Image, ImageDraw, ImageFont
def draw_emoji_on_image(image, face_location, emoji, font_path):
    top, right, bottom, left = face_location
    face_width = right - left
    face_height = bottom - top

    # 创建一个透明背景的图片
    emoji_image = Image.new('RGBA', (face_width, face_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(emoji_image)

    # 选择一个合适的字体大小
    font_size = min(face_width, face_height)
    font = ImageFont.truetype(font_path, font_size)

    # 获取文本大小和位置
    text_width, text_height = draw.textsize(emoji, font=font)
    text_x = (face_width - text_width) // 2
    text_y = (face_height - text_height) // 2

    # 在透明背景上绘制表情符号
    draw.text((text_x, text_y), emoji, font=font, fill=(255, 255, 255, 255))

    # 将 PIL 图像转换为 OpenCV 图像
    emoji_image_cv = cv2.cvtColor(np.array(emoji_image), cv2.COLOR_RGBA2BGRA)

    # 确保原始图像的对应区域与 emoji 图像尺寸相同
    image_face_region = image[top:bottom, left:right]
    if image_face_region.shape[:2] != emoji_image_cv.shape[:2]:
        # 调整 emoji 图像尺寸以匹配原始图像的对应区域
        emoji_image_cv = cv2.resize(emoji_image_cv, (image_face_region.shape[1], image_face_region.shape[0]))

    # 将调整后的 emoji 图像叠加到原始图像上
    image[top:bottom, left:right] = cv2.addWeighted(image_face_region, 0, emoji_image_cv, 1, 0)

def detect_and_fill_faces(image_path, MarkEmojis, font_path):
    # 使用 face_recognition 加载图像（以 RGB 格式）
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)

    # 将图像从 RGB 转换为 BGR
    image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # 用表情符号填充人脸区域
    for face_location in face_locations:
        emoji = np.random.choice(MarkEmojis)
        draw_emoji_on_image(image_bgr, face_location, emoji, font_path)

    # 构建输出文件路径
    base_path, ext = os.path.splitext(image_path)
    output_path = base_path + "_mark" + ext
    cv2.imwrite(output_path, image_bgr)
    print(f"Emoji marked image saved as {output_path}")

if __name__ == "__main__":
    MarkEmojis = ["🤔", "🤣", "😄", "🙂"]
    font_path = './NotoColorEmoji-Regular.ttf'  # 指定支持表情符号的字体文件路径
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        detect_and_fill_faces(image_path, MarkEmojis, font_path)
    else:
        print("Please provide an image path.")

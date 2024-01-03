import face_recognition
import sys
import cv2


def detect_and_mark_faces(image_path):
      # 使用 face_recognition 加载图像（以 RGB 格式）
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)

    # 将图像从 RGB 转换为 BGR，因为 OpenCV 默认使用 BGR
    image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # 在每个人脸周围绘制红框
    for top, right, bottom, left in face_locations:
        cv2.rectangle(image_bgr, (left, top), (right, bottom), (0, 0, 255), 2)

    # 保存修改后的图像
    ext = image_path.split(".")[-1]
    output_path = image_path + "_marked" +  "." + ext
    
    cv2.imwrite(output_path, image_bgr)
    print(f"Marked image saved as {output_path}")
    #  # 加载图片并识别人脸
    # image = face_recognition.load_image_file(image_path)
    # face_locations = face_recognition.face_locations(image)

    # # OpenCV 以 BGR 格式读取图像，因此先将其转换为 RGB
    # image_cv2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # # 在每个人脸周围绘制红框
    # for top, right, bottom, left in face_locations:
    #     cv2.rectangle(image_cv2, (left, top), (right, bottom), (0, 0, 255), 2)

    # # 将修改后的图片从 RGB 转换回 BGR 格式，并保存
    # output_image = cv2.cvtColor(image_cv2, cv2.COLOR_RGB2BGR)
    # ext = image_path.split(".")[-1]
    # output_path = image_path + "_marked" +  "." + ext
    # cv2.imwrite(output_path, output_image)
    # print(f"Marked image saved as {output_path}")

# 加载图片并识别人脸
def detect_faces(image_path):
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)

    for i, face_location in enumerate(face_locations):
        top, right, bottom, left = face_location
        print(f"Face {i + 1}:")
        print(f" - Top: {top}")
        print(f" - Right: {right}")
        print(f" - Bottom: {bottom}")
        print(f" - Left: {left}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        detect_and_mark_faces(image_path)
    else:
        print("Please provide an image path.")

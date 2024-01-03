# FaceHideEmoji

FaceHideEmoji is a unique Python tool designed for anonymizing faces in images using emojis. This innovative approach uses face detection to locate faces in an image and then overlays them with emojis, providing both privacy and a playful touch.

## Installation

Ensure Python is installed on your system before setting up FaceHideEmoji. Install the necessary dependencies with the following command:

```bash
pip install -r requirements.txt
```

This command installs all the required Python libraries, such as `face_recognition` and `opencv-python`, which are listed in `requirements.txt`.

## Usage

Run the `main.py` script with the path to the image file as an argument. The script detects human faces and covers them with emojis.

```bash
python main.py <image_path>
```

Replace `<image_path>` with the path to your image file. For example:

```bash
python main.py images/sample.jpg
```

The processed image will be saved in the same directory, indicating that the faces have been covered with emojis.

## Features

- **Automatic Face Detection**: Identifies faces in any given image.
- **Emoji Overlay**: Covers faces with emojis for an amusing yet effective way to maintain privacy.

## Contributing

Contributions to the FaceHideEmoji project are welcome. Feel free to fork the repository, make your changes, and submit a pull request for review.

## License

FaceHideEmoji is made available under the MIT License.

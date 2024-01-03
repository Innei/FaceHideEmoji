# FaceHideEmoji

FaceHideEmoji is a unique Python tool designed for anonymizing faces in images using emojis. This innovative approach uses face detection to locate faces in an image and then overlays them with emojis, providing both privacy and a playful touch.

|Before| After|
|-|-|
|![](https://private-user-images.githubusercontent.com/41265413/293907428-d6602a4c-4b00-4179-b490-9dfe9459df80.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDQyODM1MTAsIm5iZiI6MTcwNDI4MzIxMCwicGF0aCI6Ii80MTI2NTQxMy8yOTM5MDc0MjgtZDY2MDJhNGMtNGIwMC00MTc5LWI0OTAtOWRmZTk0NTlkZjgwLmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAxMDMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMTAzVDEyMDAxMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTgxNDBiYTgyMTlkYmM5NjFjNmVlZmQ0OGVmMjYwZDU0NTdkOTcxZjNkN2Q3Mzc0ZDU2MDI3MGM2Njk2MTdiZWEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.hmYOBfhuY4Y2odrTSppcNUKHx1I6vd_w3kwpdDirnMc) | ![](https://private-user-images.githubusercontent.com/41265413/293907421-bc2164d3-8820-4fad-844d-83c78edec5bf.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDQyODM1MTAsIm5iZiI6MTcwNDI4MzIxMCwicGF0aCI6Ii80MTI2NTQxMy8yOTM5MDc0MjEtYmMyMTY0ZDMtODgyMC00ZmFkLTg0NGQtODNjNzhlZGVjNWJmLmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAxMDMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMTAzVDEyMDAxMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTYxMTJhYjUzYjBlYzE4MDRlNzc4YzAzM2MyOWQxYmZjOTE3ZWY0MDI0MWRkM2VhODQ5YjM4ZWRiODVkNGE2N2MmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.ga8MUgnfwrkEq6x3o7Cu8Dpb9nN-LmVqvgZQFKy-To0)|

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

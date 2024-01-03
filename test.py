from pilmoji import Pilmoji
from PIL import Image, ImageFont
from PIL import Image, ImageDraw, ImageFont

my_string = '''😎'''

# with Image.new('RGB', (550, 80), (255, 255, 255)) as image:
#     font = ImageFont.truetype('./Arial.ttf', 24)

#     with Pilmoji(image) as pilmoji:
#         pilmoji.text((10, 10), my_string.strip(), (0, 0, 0), font)

#     image.show()

font = ImageFont.truetype('./Arial.ttf', 200)
emoji_image = Image.new('RGBA', (200, 200), (0, 0, 0, 0))
# draw = ImageDraw.Draw(emoji_image)
pilmoji = Pilmoji(emoji_image)
pilmoji.text((10, 10), my_string.strip(), (0, 0, 0), font)
emoji_image.show()
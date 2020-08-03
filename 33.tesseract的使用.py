import pytesseract
from PIL import Image

# 加载文件
img = Image.open('timg2.jpg')
# 识别文字
str = pytesseract.image_to_string(img)
print(str)
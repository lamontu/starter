from PIL import Image
import locale
from contextlib import contextmanager

@contextmanager
def c_locale():
    try:
        currlocale = locale.getlocale()
    except ValueError:
        currlocale = ('en_US', 'UTF-8')
    locale.setlocale(locale.LC_ALL, "C")
    yield
    locale.setlocale(locale.LC_ALL, currlocale)

image = Image.open('./images/cellflow0_corner.png')

with c_locale():
    from tesserocr import PyTessBaseAPI
    with PyTessBaseAPI() as api:
        api.SetImage(image)
        size = image.size
        w = size[0]//3
        h = size[1]//4
        # api.SetRectangle(45, 20, w, h)
        # ocrResult = api.GetUTF8Text()
        # print(ocrResult)
        # conf = api.MeanTextConf()
        area = (7, 7, w, h)
        cropped_img = image.crop(area)
        cropped_img.show()
        crop_name = "./images/cellflow0_corner_text.png"
        cropped_img.save(crop_name)
        api.SetImageFile(crop_name)
        text = api.GetUTF8Text()
        print(text)
        conf = api.MeanTextConf()
        print(conf)
    
    
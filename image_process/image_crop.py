from PIL import Image
import numpy as np


image=Image.open('./images/cellflow.jpg')
image.load()

image_data = np.asarray(image)
image_data_bw = image_data.max(axis=2)
non_empty_columns = np.where(image_data_bw.min(axis=0)<255)[0]
non_empty_rows = np.where(image_data_bw.min(axis=1)<255)[0]
cropBox = (min(non_empty_rows) - 4, max(non_empty_rows) - 6, min(non_empty_columns), max(non_empty_columns) + 4)

image_data_new = image_data[cropBox[0]:cropBox[1], cropBox[2]:cropBox[3], :]

new_image = Image.fromarray(image_data_new)
new_image.save('./images/cellflow_cropped_border.jpg')


# imageBox = image.getbbox()
# cropped=image.crop(imageBox)
# cropped.save('./images/cropped2.png')
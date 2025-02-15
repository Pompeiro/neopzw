import easyocr
from PIL import Image

LEFT_SIDE_NICKS_TOP_LEFT_CORNER = (190, 210)
LEFT_SIDE_NICKS_BOTTOM_RIGHT_CORNER = (420, 660)

LEFT_TO_RIGHT_NICKS_SHIFT_X = 650


RIGHT_SIDE_NICKS_TOP_LEFT_CORNER = (LEFT_SIDE_NICKS_TOP_LEFT_CORNER[0] + LEFT_TO_RIGHT_NICKS_SHIFT_X, 210)
RIGHT_SIDE_NICKS_BOTTOM_RIGHT_CORNER = (LEFT_SIDE_NICKS_BOTTOM_RIGHT_CORNER[0] + LEFT_TO_RIGHT_NICKS_SHIFT_X, 660)
image1= 'screenshots/w31.png'
with Image.open(image1) as image:
    image_crop_left = image.crop(box=(LEFT_SIDE_NICKS_TOP_LEFT_CORNER[0],LEFT_SIDE_NICKS_TOP_LEFT_CORNER[1],LEFT_SIDE_NICKS_BOTTOM_RIGHT_CORNER[0], LEFT_SIDE_NICKS_BOTTOM_RIGHT_CORNER[1]))
    image_crop_left.save('screenshots/w31_crop_left.png')

    image_crop_right = image.crop(box=(RIGHT_SIDE_NICKS_TOP_LEFT_CORNER[0],LEFT_SIDE_NICKS_TOP_LEFT_CORNER[1],RIGHT_SIDE_NICKS_BOTTOM_RIGHT_CORNER[0], RIGHT_SIDE_NICKS_BOTTOM_RIGHT_CORNER[1]))
    image_crop_right.save('screenshots/w31_crop_right.png')

reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
result_left = reader.readtext('screenshots/w31_crop_left.png',detail=0)
result_right = reader.readtext('screenshots/w31_crop_right.png',detail=0)


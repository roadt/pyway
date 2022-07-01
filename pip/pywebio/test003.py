from pywebio.input import *

img = file_upload("Select a image:", accept='image/*')
print(type(img), img.keys())


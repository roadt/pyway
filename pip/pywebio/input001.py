

from pywebio.input import *

age = input("How old ar you?", type=NUMBER)

password = input("Input password", type=PASSWORD)

gift = select("Which gift you want?", ['keyboard', 'ipad'])

agree = checkbox('User Term', options=['I agree to terms and conditions'])

answer = radio("Choose one", options=['A', 'B', 'C', 'D'])

text = textarea("TextArea", rows=3, placeholder="Some text")

img = file_upload("Select a image:", accept='image/*')



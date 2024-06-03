import secrets
import os
from PIL import Image
from flask import current_app

def save_picture(picture):
    random = secrets.token_hex(8)
    _, file_ext = os.path.splitext(picture.filename)
    picture_file_name = random + file_ext
    picture_path = os.path.join(current_app.root_path,'static/images/profile_pictures',picture_file_name)
    size = (250,250)
    img = Image.open(picture)
    img.thumbnail(size)
    img.save(picture_path)
    return picture_file_name


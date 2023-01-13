from flask import Blueprint, render_template, request, current_app

from loader.utils import save_picture
from main.utils import PostsHandler
import logging

logging.basicConfig(handlers=[logging.FileHandler(filename='basic.log', encoding='utf-8', mode='a+')], level=logging.INFO)

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')

@loader_blueprint.route('/post')
def create_new_post_page():
    return render_template('post_form.html')

@loader_blueprint.route('/post', methods=['POST'])
def create_new_post_from_user_data_page():
    content = request.form.get('content')
    picture = request.files.get('picture')
    picture_path = save_picture(picture)

    if not picture or not content:
        return 'Данные не получены'
    if not save_picture(picture):
        text_error = f'Файл {picture.filename}- не изображение'
        logging.info(text_error)
        return text_error

    posts_handler = PostsHandler(current_app.config['POST_PATH'])
    new_post = {'pic' : picture_path, 'content' : content}
    error = posts_handler.add_post(new_post)
    if error:
        logging.error(f'Ошибка загрузки поста')
        return "Ошибка загрузки"
    return render_template('post_uploaded.html', content=content, picture_path=picture_path)

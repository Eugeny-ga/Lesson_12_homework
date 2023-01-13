from flask import Blueprint, render_template, request, current_app
from main.utils import PostsHandler
import logging

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename='basic.log', level=logging.INFO)


@main_blueprint.route('/')
def page_index():
    return render_template('index.html')

@main_blueprint.route('/search')
def search_page():
    search_words = request.args.get('s')

    logging.info(f'Поиск {search_words}')

    all_posts = PostsHandler(current_app.config['POST_PATH'])
    posts = all_posts.search_posts_from_data_posts(search_words)

    return render_template('post_list.html', search_words=search_words, posts=posts)


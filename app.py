from flask import Flask, send_from_directory
from main.view import main_blueprint
from loader.view import loader_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.config['POST_PATH'] = POST_PATH

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

@app.route('/uploads/<path:path>')
def static_dir(path):
    return send_from_directory('uploads', path)


app.run()



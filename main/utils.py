import json



class PostsHandler:

    def __init__(self, path):
        self.path = path

    def load_posts_from_json(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            posts = json.load(file)
        return posts

    def search_posts_from_data_posts(self, search_words):
        posts = self.load_posts_from_json()
        search_posts = []
        for post in posts:
            if search_words.lower() in post['content'].lower():
                search_posts.append(post)

        return search_posts

    def save_posts_to_json(self, posts):
        try:
            with open(self.path, 'w', encoding='utf-8') as file:
                json.dump(posts, file, ensure_ascii=False)
        except Exception as e:
            return e

    def add_post(self, post):
        posts = self.load_posts_from_json()
        posts.append(post)
        self.save_posts_to_json(posts)

from flask import render_template


def get_urls(app, data):
    @app.route('/')
    def hello_world():
        return render_template('index.html', title=data["title"], subtitle=data["subtitle"])
    @app.route('/test')
    def test():
        return render_template('test.html', title=data["title"], subtitle=data["title"])
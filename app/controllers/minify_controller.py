from app import app
from app.models.user_models import MinifiedUrl


@app.route('/url', methods=['POST'])
def minify_url():
    print("helloomar")
    minified_url = MinifiedUrl(url="www.google.com")
    app.db.session.add(minified_url)
    app.db.session.commit()


@app.route('/')
def version():
    return '1.0.0'

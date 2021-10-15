from app import app, db
from app.models import User, Post

if __name__ == '__main__':
    app.run()
@app.shell_context_processor
def make_shell_content():
    return {'db': db, 'User': User, 'Post': Post}

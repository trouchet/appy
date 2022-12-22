from flask import Blueprint

posts_bp = Blueprint('posts', __name__)


@posts_bp.route('/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

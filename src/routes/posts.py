import sys
 
# setting path
sys.path.append('../')

from appy import app

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

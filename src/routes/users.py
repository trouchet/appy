import sys
 
# setting path
sys.path.append('../')

from appy import app


@app_y.route('/users/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

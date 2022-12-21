import sys
 
# setting path
sys.path.append('../')

from appy import app


@app.route('/about')
def about():
    return 'The about page'


@app.route('/login', methods=['GET', 'POST'])
def do_login():
    if request.method == 'POST':
        return 'do login'
    else:
        return 'show login form'


@app.route('/hello/')
@app.route('/hello/<name>')
def say_hello(name=None):
    if(name is None):
        return 'Hello, World!'
    else:
        return f"Hello, {escape(name)}!"    


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'



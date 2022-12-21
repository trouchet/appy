import sys
 
# setting path
sys.path.append('../')

from appy import app


@app.route('/projects/')
def show_projects():
    return 'The project page'



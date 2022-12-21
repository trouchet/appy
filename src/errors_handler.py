from . import app_y

@app_y.errorhandler(404)
def page_not_found(error):
    return 'Error 404'
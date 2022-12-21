from flask import Blueprint


blueprint = Blueprint(
	'simple_page', 
	__name__, 
	template_folder='../templates'
)

@blueprint.route('/')
def index():
    return 'Index Page'



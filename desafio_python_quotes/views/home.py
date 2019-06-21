from pyramid.view import view_config

from desafio_python_quotes.service.session_service import set_session


@view_config(route_name='home', renderer='../templates/home.jinja2')
def home_view(request):
    set_session(request)
    return dict()

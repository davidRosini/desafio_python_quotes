from pyramid.view import view_config

import random

from desafio_python_quotes.service.quotes_service import get_quotes, get_quote
from desafio_python_quotes.service.session_service import set_session


@view_config(route_name='quotes', renderer='../templates/quotes.jinja2')
def list_quotes(request):
    set_session(request)
    return {'quotes': get_quotes()['quotes']}


@view_config(route_name='quote_random', renderer='../templates/quote.jinja2')
def show_quote_random(request):
    set_session(request)
    quotes = get_quotes()['quotes']
    max_itens = len(quotes)
    rand_item = random.randint(0, max_itens)
    return {'quote_number': rand_item,
            'quote': quotes[rand_item]}


@view_config(route_name='quote', renderer='../templates/quote.jinja2')
def show_quote(request):
    set_session(request)
    return {'quote_number': request.matchdict['quote_number'],
            'quote': get_quote(request.matchdict['quote_number'])['quote']}

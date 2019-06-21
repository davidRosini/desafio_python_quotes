from pyramid.view import view_config

from desafio_python_quotes.models.history_session import HistorySession


@view_config(route_name='visits_session', renderer='json')
def list_history_session(request):
    result = request.dbsession.query(HistorySession).order_by(HistorySession.uuid).all()
    return {'visits': list_history_to_json(result)}


@view_config(route_name='history_session', renderer='json')
def list_visits_session(request):
    result = request.dbsession.query(HistorySession).filter(HistorySession.uuid == request.session['session']['uuid']) \
        .all()
    return {'history': list_history_to_json(result)}


def list_history_to_json(list_history):

    array_hist = []
    for history in list_history:
        array_hist.append({
            'id': history.id,
            'uuid': history.uuid,
            'datetime': history.datetime.strftime('%x %X'),
            'page': history.page
        })

    return array_hist

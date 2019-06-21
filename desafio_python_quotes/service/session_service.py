import uuid
import datetime

from desafio_python_quotes.models.history_session import HistorySession


def add_session(request):
    session = request.session['session']
    history_session = HistorySession(uuid=session['uuid'], datetime=session['datetime'], page=session['page'])
    request.dbsession.add(history_session)


def set_session(request):
    session = request.session

    if 'session' not in session:
        session['session'] = {
            'uuid': uuid.uuid4().hex,
            'datetime': '',
            'page': ''
        }

    session['session']['datetime'] = datetime.datetime.now()
    session['session']['page'] = request.path_url

    add_session(request)

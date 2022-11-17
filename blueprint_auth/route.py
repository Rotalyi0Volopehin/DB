from flask import Blueprint, request, render_template, current_app, session, redirect, url_for
from typing import Optional, Dict
from sql_provider import SQLProvider
from db_work import select_dict
import os


blueprint_auth = Blueprint('bp_auth', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@blueprint_auth.route('/')
def start_auth():
    return render_template('start_auth.html')


@blueprint_auth.route('/login', methods=['GET', 'POST'])
def authentication():
    if request.method == 'GET':
        return render_template('input_login.html')
    else:
        login = request.form.get('login')
        password = request.form.get('password')
        if login:
            user_info = define_user(login, password)
            if user_info:
                user_dict = user_info[0]
                session['user_id'] = user_dict['user_id']
                session['user_group'] = user_dict['user_group']
                session.permanent = True
                return redirect(url_for('start_func'))
            else:
                return render_template('input_login.html', error='Пользователь не найден')
        return render_template('input_login.html', error='Повторите ввод')


def define_user(login: str, password: str) -> Optional[Dict]:
    sql_internal = provider.get('internal_user.sql', login=login, password=password)
    sql_external = provider.get('external_user.sql', login=login, password=password)
    for sql_search in [sql_internal, sql_external]:
        user_info = select_dict(current_app.config['dbconfig'], sql_search)
        if user_info:
            break
    return user_info

#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''date: 2021-11-15
'''

import functools

from flask import (Blueprint, flash, g, redirect, render_template, request,
                   session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'username is required'
        elif not password:
            error = 'password is required'

        if error is None:
            try:
                db.execute('', (username, generate_password_hash(password)))
                db.commit()
            except db.IntegrityError:
                error = ''
            else:
                return redirect(url_for('auth.login'))

        flash(error)
    return render_template('auth/register.html')

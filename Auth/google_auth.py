from authlib.integrations.flask_client import OAuth
from flask import redirect, url_for, session
from Config.database_connection import create_connection

oauth = OAuth()

def init_google_oauth(app):
    oauth.init_app(app)
    oauth.register(
        name='google',
        client_id=app.config['GOOGLE_CLIENT_ID'],
        client_secret=app.config['GOOGLE_CLIENT_SECRET'],
        authorize_url='https://accounts.google.com/o/oauth2/auth',
        access_token_url='https://oauth2.googleapis.com/token',
        api_base_url='https://www.googleapis.com/oauth2/v1/',
        client_kwargs={'scope': 'openid email profile'},
    )

def login_google():
    return oauth.google.authorize_redirect(
        redirect_uri=url_for('auth.google_callback', _external=True)
    )

def google_callback():
    token = oauth.google.authorize_access_token()
    user = oauth.google.get('userinfo').json()

    conn = create_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT * FROM usuarios WHERE correo=%s", (user['email'],))
    usuario = cur.fetchone()

    if not usuario:
        cur.execute("""
            INSERT INTO usuarios (nombre, correo, google_id, rol, auth_provider)
            VALUES (%s, %s, %s, 'estudiante', 'google')
        """, (user['name'], user['email'], user['id']))
        conn.commit()

        cur.execute("SELECT * FROM usuarios WHERE correo=%s", (user['email'],))
        usuario = cur.fetchone()

    session['usuario'] = {
        'id': usuario['id'],
        'nombre': usuario['nombre'],
        'tipo': usuario['rol']
    }

    cur.close()
    conn.close()

    return redirect("/home")

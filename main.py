from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from Config.config import Config
from Auth.google_auth import init_google_oauth

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_google_oauth(app)

    from Routes.auth_routes import auth_bp
    from Routes.estudiante_routes import estudiante_bp
    from Routes.admin_routes import admin_bp
    from Routes.profesor_routes import profesor_bp
    from Routes.padre_routes import padre_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(estudiante_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(profesor_bp)
    app.register_blueprint(padre_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

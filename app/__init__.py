from flask import Flask
# from app.routes.financial_reports import financial_reports_bp

def create_app():
    app = Flask(__name__)

    # Register blueprints
    # app.register_blueprint(financial_reports_bp, url_prefix='/ocr')

    return app
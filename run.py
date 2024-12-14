from app.services.logging_service import LoggerService
from flask import Flask
# from app.routes.financial_reports import financial_reports_bp
from app.routes.web_routes import web_bp
from app.routes.api_routes import api_bp

# Inisialisasi logger
logger_service = LoggerService()
logger = logger_service.get_logger()

logger.info('Aplikasi dimulai...')

app = Flask(__name__, template_folder='app/templates', static_folder='app/resources')

# Register Blueprint
# app.register_blueprint(financial_reports_bp)
app.register_blueprint(web_bp)
app.register_blueprint(api_bp, url_prefix='/api/ocr')

if __name__ == '__main__':
    app.run(debug=True)


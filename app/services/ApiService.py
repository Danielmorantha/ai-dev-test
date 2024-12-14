from app.config import Config
import requests
import os, json
from app.services.logging_service import LoggerService
from app.middleware.token_verify import TokenService
from datetime import datetime


logger_service = LoggerService()
logger = logger_service.get_logger()

class ApiService:
    def __init__(self):
        self.data_folder = os.path.dirname(os.path.abspath(__file__))
        self.token_service = TokenService()
        self.url = None

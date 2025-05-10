import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-123')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///sistema_ventas.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
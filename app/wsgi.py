from dotenv import load_dotenv

from .app import create_app

load_dotenv("../.flaskenv")
app = create_app()

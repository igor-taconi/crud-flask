from dotenv import load_dotenv

from app import create_app
from app.settings import env_file

load_dotenv(env_file)

app = create_app()

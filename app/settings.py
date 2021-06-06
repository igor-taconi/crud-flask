from os.path import join
from pathlib import Path
from typing import NoReturn

from dynaconf import Dynaconf, FlaskDynaconf
from flask import Flask

settings = Dynaconf(
    settings_files=['settings.toml', '.secrets.toml'],
    load_dotenv=True,
)

base_dir = Path(__file__).resolve().parent.parent

env_file = join(base_dir, '.env')


def init_app(app: Flask) -> NoReturn:
    FlaskDynaconf(app)

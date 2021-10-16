import os
import dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dotenv_file = os.path.join(BASE_DIR, ".env")

if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)
    CLIENT_ID = os.environ.get('CLIENT_ID')
    EMAIL = os.environ.get('EMAIL')
    NAME = os.environ.get('NAME')
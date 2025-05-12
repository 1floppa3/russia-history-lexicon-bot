import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / '.env')

BOT_TOKEN: str = os.getenv('BOT_TOKEN')
WORDS_DB_FILE: Path = Path(__file__).parent.parent / 'data' / 'words.json'
USER_DATA_DB_FILE = Path(__file__).parent.parent / 'data' / "users.json"

import requests
import json as jsonlib

from constants import DB_NAME, DB_API_URL
from os.path import exists
from utils import (
  load_file,
  save_sha,
  to_sha_path,
  read_sha
)

def check_updates() -> bool:
  request = requests.get(DB_API_URL)
  json = jsonlib.loads(request.content)
  for entry in json:
    if entry['name'] == DB_NAME:
      if not exists(DB_NAME) or not exists(to_sha_path(DB_NAME)):
        load_file(entry['download_url'], DB_NAME)
        save_sha(DB_NAME, entry['sha'])
      local_sha = read_sha(DB_NAME)
      if local_sha != entry['sha']:
        load_file(entry['download_url'], DB_NAME)
        save_sha(DB_NAME, entry['sha'])
      break
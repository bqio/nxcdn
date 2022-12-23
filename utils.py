import requests
import json

def load_file(url: str, filename: str) -> None:
  request = requests.get(url)
  with open(filename, "wb") as f:
    f.write(request.content)

def save_sha(filename: str, sha: str) -> None:
  with open(to_sha_path(filename), "w") as f:
    f.write(sha)

def read_sha(filename: str) -> str:
  with open(to_sha_path(filename), "r") as f:
    return f.read()

def to_sha_path(path: str) -> str:
  return f'{path}.sha.txt'

def read_json(filename: str) -> any:
  with open(filename, "rb") as f:
    return json.load(f)

def save_list(filename: str, _list: list) -> None:
  with open(filename, "w") as f:
    f.write('\n'.join(_list))
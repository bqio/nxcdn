import requests

from constants import DB_NAME
from os import makedirs
from PIL import Image
from io import BytesIO
from os.path import exists
from utils import read_json

def sync_images():
  json = read_json(DB_NAME)
  for key in json:
    title = json[key]
    if title and title['id']:
      title_path = f"titles/{title['id']}"
      try:
        makedirs(title_path)
      except OSError:
        pass
      if title['bannerUrl'] and not exists(f"{title_path}/banner.webp"):
        convert_image(title['bannerUrl'], f"{title_path}/banner.webp", "webp", 30)
      if title['iconUrl'] and not exists(f"{title_path}/icon.webp"):
        convert_image(title['iconUrl'], f"{title_path}/icon.webp", "webp", 30)
      if title['screenshots']:
        for n, src in enumerate(title['screenshots']):
          if not exists(f"{title_path}/{n}.webp"):
            convert_image(src, f"{title_path}/{n}.webp", "webp", 30)

def convert_image(src: str, dst: str, fmt: str, qual: int):
  request = requests.get(src)
  source_image = Image.open(BytesIO(request.content))
  source_image.save(dst, format=fmt, quality=qual)
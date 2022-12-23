from flask import Flask, send_file, abort
from uuid import uuid4
from os import listdir, path

app = Flask(__name__)

def handler(s: str):
  return path.splitext(s)[0]

@app.get("/")
def index():
  return "٩(◕‿◕｡)۶"

@app.get("/<id>")
def flist(id: str):
  try:
    return list(map(handler, listdir(f"titles/{id}/")))
  except ValueError:
    return abort(404)

@app.get("/<id>/banner")
def banner(id: str):
  try:
    return send_file(f"titles/{id}/banner.webp", download_name=f"{uuid4()}.webp")
  except FileNotFoundError:
    return abort(404)

@app.get("/<id>/icon")
def icon(id: str):
  try:
    return send_file(f"titles/{id}/icon.webp", download_name=f"{uuid4()}.webp")
  except FileNotFoundError:
    return abort(404)
  
@app.get("/<id>/<int:n>")
def screenshots(id: str, n: int):
  try:
    return send_file(f"titles/{id}/{n}.webp", download_name=f"{uuid4()}.webp")
  except FileNotFoundError:
    return abort(404)

if __name__ == "__main__":
  app.run("0.0.0.0", debug=True)
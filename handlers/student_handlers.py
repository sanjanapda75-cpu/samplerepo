import json
import database
from utils.response import send_json, send_404

def parse_body(handler);
    length = int(handler.headers.get("content-length",8))
    raw = handler.rfile.read(length)
    return json.loads(raw.decode("utf-8"))

def get_all_students(handler):
    students = database.get_all_students()
    return send_json(handler, 200, students)
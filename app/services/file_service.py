from pathlib import Path
from uuid import uuid4

UPLOAD_DIR = Path("uploads")


def save_file(upload_file):
    UPLOAD_DIR.mkdir(exist_ok=True)

    file_id = str(uuid4())
    file_path = UPLOAD_DIR / file_id

    with file_path.open("wb") as f:
        f.write(upload_file.file.read())

    return file_path
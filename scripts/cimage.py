import tempfile
from ifnude import detect

def convert_to_sd(img):
    shapes = []
    chunks = detect(img)
    for chunk in chunks:
        shapes.append(False)
    return [any(shapes), tempfile.NamedTemporaryFile(delete=False, suffix=".png")]

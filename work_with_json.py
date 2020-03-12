import json
from pathlib import Path


data = Path('Movies.json').read_text()
movies = json.loads(data)
print(movies)

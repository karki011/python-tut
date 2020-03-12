from pathlib import Path
from zipfile import ZipFile

with ZipFile("testZip.zip", "w") as zip:
    for path in Path('test').rglob("*.*"):
        zip.write(path)

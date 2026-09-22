from pathlib import Path
from urllib.request import urlretrieve

URL = "https://raw.githubusercontent.com/yufung/ab-testing-cookie-cats/master/data/cookie_cats.csv"
TARGET = Path(__file__).parent / "data" / "cookie_cats.csv"
TARGET.parent.mkdir(exist_ok=True)

print(f"Downloading Cookie Cats dataset to {TARGET} ...")
urlretrieve(URL, TARGET)
print("Done.")

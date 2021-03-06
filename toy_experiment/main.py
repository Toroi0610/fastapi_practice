from pathlib import Path
from tqdm import tqdm

from uploader import uploader
from reader import reader


url = 'http://127.0.0.1:80/processing-add/'
upload_csv_dir = Path("toy_dataset")

res = uploader(url, [filename.as_posix() for filename in upload_csv_dir.glob("input_*.csv")])

for key, value in tqdm(res.items()):
    output_filename = "toy_download/processed_" + key.split("/")[-1]
    reader(value, output_filename)
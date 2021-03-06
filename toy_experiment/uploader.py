from pathlib import Path
from subprocess import Popen

upload_csv_dir = Path("toy_dataset")

for upload_csv in upload_csv_dir.glob("*.csv"):
    Popen(f'curl -X POST "http://127.0.0.1:80/processing-add/" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -F "file=@{upload_csv.as_posix()}.csv" -o "/toy_download/{upload_csv.name[:-4]}_add_x_plus_y.json"')

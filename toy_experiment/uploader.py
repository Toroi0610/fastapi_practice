import requests
from tqdm import tqdm
def uploader(url,
             upload_csvs
             ):

    upload_file = {}
    output_json = {}
    for f in tqdm(upload_csvs):
        with open(f, "rb") as f:
            upload_file["file"] = f.read()

        res = requests.post(url, files=upload_file)
        output_json[f.name] = res.json()
    return output_json

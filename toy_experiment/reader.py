from pandas import read_json

def reader(res_json, output_filename):
    result = read_json(res_json)
    result.to_csv(output_filename, index=False)
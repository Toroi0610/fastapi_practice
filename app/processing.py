import pandas as pd

def add(data_string):
    data_list = [k.split(",") for k in data_string.split("\n") if k != ""]
    data_header, data_values = data_list[0], [list(map(float, k)) for k in data_list[1:]]
    data = pd.DataFrame(data_values, columns=data_header)
    data["x+y"] = data["x"]+data["y"]
    # return data.to_csv(index=False)
    return data.to_json()
import json


# 读取json文件
def get_json_data(file_path):
    with(open(file_path, "r")) as f:
        json_data = json.loads(f.read())
    return json_data




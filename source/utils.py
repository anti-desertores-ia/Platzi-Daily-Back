import json


def get_json_dict(path: str) -> dict:
    file = open(path, "r")
    data = json.loads(file.read())
    file.close()

    return data

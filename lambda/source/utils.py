import json
import boto3


def get_json_dict(path: str) -> dict:
    file = open(path, "r")
    data = json.loads(file.read())
    file.close()

    return data


def get_secure_string_ssm_param(name: str):
    ssm_client = boto3.client("ssm", region_name="us-east-1")

    response = ssm_client.get_parameter(Name=name, WithDecryption=True)

    return response.get("Parameter", {}).get("Value", "")


def get_string_ssm_param(name: str):
    ssm_client = boto3.client("ssm", region_name="us-east-1")

    response = ssm_client.get_parameter(Name=name, WithDecryption=True)

    return response.get("Parameter", {}).get("Value", "")

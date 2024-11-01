import json

from typing import Any
from source.utils import get_json_dict
from source.config import LOGGER
from source import controller


def lambda_handler(event: dict, context: Any):
    result = None

    try:
        path = event.get("path", "")
        method = event.get("method", "")
        body = json.loads(event.get("body", "{}"))

        result = router(path=path, method=method, **body)
    except Exception as e:
        LOGGER.error(f"Something went wrong: {e}")

    return json.dumps(
        {"statusCode": 200 if result is not None else 500, "body": result}
    )


def router(path: str, method: str, *args, **kwargs) -> dict:
    routes = get_json_dict("source/data/routes.json")

    path_function_name = routes.get(method, {}).get(path, "empty")

    return getattr(controller, path_function_name)(*args, **kwargs)
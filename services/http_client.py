import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def get_json(base_url: str, path: str, default=None):
    url = f"{base_url.rstrip('/')}{path}"
    try:
        request = Request(url, headers={"Accept": "application/json"})
        with urlopen(request, timeout=2) as response:
            return json.loads(response.read().decode("utf-8"))
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError):
        return default


def post_json(base_url: str, path: str, payload: dict, default=None):
    url = f"{base_url.rstrip('/')}{path}"
    try:
        data = json.dumps(payload).encode("utf-8")
        request = Request(
            url,
            data=data,
            headers={"Accept": "application/json", "Content-Type": "application/json"},
            method="POST",
        )
        with urlopen(request, timeout=2) as response:
            return json.loads(response.read().decode("utf-8"))
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError):
        return default

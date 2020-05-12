from dataclasses import dataclass
from typing import Any, Optional

import requests
import ujson


@dataclass
class Request:
    status: int
    data: Any


class Web:
    # TODO proxy support
    def __init__(self, headers: Optional[dict] = None, timeout: Optional[int] = None):
        self.session: object = requests.Session()
        if headers:
            self.session.headers.update(headers)
        # TODO actually use this
        self.timeout: int = timeout



def get(url: str, session: Optional[Web] = None, json: bool = False) -> Request:
    if session is not None:
        req = session.session.get(url=url, timeout=session.timeout)
    else:
       req = requests.get(url=url)

    status = req.status_code
    if status != 200:
        return Request(status, None)
    elif json:
        return Request(status, todict(req.text))
    else:
        return Request(status, req.text)


def post(url: str, data: dict, session: Optional[Web] = None) -> Request:
    if session is not None:
        session.session.post(url=url, data=data, timeout=session.timeout)
    else:
        req = requests.post(url=url, data=data)
    status = req.status_code
    if status:
        return Request(status, None)
    else:
        return Request(status, req.text)


# maybe move this to utils or something
def todict(text: str) -> Any:
    if _j := ujson.loads(text):
        return _j
    else:
        return None

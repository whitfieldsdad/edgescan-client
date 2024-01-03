import datetime
import os
from typing import Union


TIMESTAMP = Union[str, int, float, datetime.date, datetime.datetime]

DEFAULT_HOST = os.getenv("EDGESCAN_HOST", "live.edgescan.com")
DEFAULT_API_KEY = os.getenv("EDGESCAN_API_KEY")

HOSTS = "hosts"
ASSETS = "assets"
VULNERABILITIES = "vulnerabilities"
SERVICES = "services"

OBJECT_TYPES = {
    HOSTS,
    ASSETS,
    VULNERABILITIES,
    SERVICES,
}

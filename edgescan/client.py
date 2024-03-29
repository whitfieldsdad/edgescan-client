from dataclasses import dataclass
import json
import os
from typing import Iterator, Optional
from requests import Session
import urllib.parse
import logging

from edgescan.constants import DEFAULT_API_KEY, DEFAULT_HOST, OBJECT_TYPES, TIMESTAMP

logger = logging.getLogger(__name__)


@dataclass()
class Client:
    host: str = DEFAULT_HOST
    api_key: str = DEFAULT_API_KEY

    def __post_init__(self) -> None:
        self.session = Session()
        self.session.headers.update({
            "X-Api-Token": self.api_key,
            "Content-Type": "application/json",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
        })

    @property
    def url(self) -> str:
        return "https://" + self.host

    def get_download_url(self, object_type: str) -> str:
        return urllib.parse.urljoin(self.url, f"api/v1/{object_type}.json")

    def get_object(self, object_type: str, object_id: int) -> Optional[dict]:
        rows = self.iter_objects(object_type=object_type, ids=[object_id])
        return next(rows, None)

    def iter_objects(self, object_type: str) -> Iterator[dict]:
        url = self.get_download_url(object_type)

        response = self.session.get(url)
        response.raise_for_status()

        for row in response.json()[object_type]:
            if row:
                yield row

    def count_objects(self, object_type: str) -> int:
        rows = self.iter_objects(object_type=object_type)
        return sum(1 for _ in rows)

    def export_objects(self, object_type: str, path: str):
        with open(path, "w") as file:
            for row in self.iter_objects(object_type=object_type):
                line = json.dumps(row) + "\n"
                file.write(line)

    def export_all_objects(self, output_dir: str):
        for object_type in OBJECT_TYPES:
            path = os.path.join(output_dir, f"{object_type}.jsonl")
            self.export_objects(object_type=object_type, path=path)

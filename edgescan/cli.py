import datetime
import itertools
import json
import logging
from typing import List, Optional

import click

import edgescan.time
from edgescan.client import Client
from edgescan.constants import OBJECT_TYPES, OBJECT_TYPES

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


@click.group()
def cli():
    """
    Edgescan API client.
    """


@cli.command("get")
@click.argument("object_type", type=click.Choice(OBJECT_TYPES), required=True)
@click.argument("object_id", type=int, required=True)
def get_object(object_type: int, object_id: int):
    """
    Lookup objects.
    """
    api = Client()
    row = api.get_object(object_type=object_type, object_id=object_id)
    if row:
        print(json.dumps(row))


@cli.command("list")
@click.argument("object_type", type=click.Choice(OBJECT_TYPES), required=True)
@click.option("--id", "ids", multiple=True)
@click.option("--min-create-time", type=edgescan.time.to_datetime)
@click.option("--max-create-time", type=edgescan.time.to_datetime)
@click.option("--min-update-time", type=edgescan.time.to_datetime)
@click.option("--max-update-time", type=edgescan.time.to_datetime)
@click.option("--limit", type=int)
def get_objects(
    object_type: int,
    ids: List[str],
    min_create_time: Optional[datetime.datetime],
    max_create_time: Optional[datetime.datetime],
    min_update_time: Optional[datetime.datetime],
    max_update_time: Optional[datetime.datetime],
    limit: Optional[int] = None,
):
    """
    List objects.
    """
    api = Client()
    rows = api.iter_objects(
        object_type=object_type,
        ids=ids,
        min_create_time=min_create_time,
        max_create_time=max_create_time,
        min_update_time=min_update_time,
        max_update_time=max_update_time,
    )
    for row in itertools.islice(rows, limit):
        print(json.dumps(row))


@cli.command("count") 
@click.argument("object-type", type=click.Choice(OBJECT_TYPES), required=True)
@click.option("--id", "ids", multiple=True)
@click.option("--min-create-time", type=edgescan.time.to_datetime)
@click.option("--max-create-time", type=edgescan.time.to_datetime)
@click.option("--min-update-time", type=edgescan.time.to_datetime)
@click.option("--max-update-time", type=edgescan.time.to_datetime)
def count_objects(
    object_type: str,
    ids: List[str],
    min_create_time: Optional[datetime.datetime],
    max_create_time: Optional[datetime.datetime],
    min_update_time: Optional[datetime.datetime],
    max_update_time: Optional[datetime.datetime]):
    """
    Count objects.
    """
    api = Client()
    total = api.count_objects(
        object_type=object_type,
        ids=ids,
        min_create_time=min_create_time,
        max_create_time=max_create_time,
        min_update_time=min_update_time,
        max_update_time=max_update_time,
    )
    print(total)


@cli.command("export")
@click.argument("object-type", type=click.Choice(OBJECT_TYPES | {'all'}), required=True)
@click.argument("path", required=True)
def export_objects(object_type: Optional[str], path: str):
    """
    Export objects to a file (JSONL).
    """
    api = Client()
    if object_type == 'all':
        api.export_all_objects(output_dir=path)
    else:
        api.export_objects(object_type=object_type, path=path)


if __name__ == "__main__":
    cli()

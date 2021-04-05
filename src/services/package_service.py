import datetime
from typing import List, Optional

from src.data.package import Package
from src.data.release import Release


def release_count() -> int:
    return 2_234_847


def package_count() -> int:
    return 274_000


def latest_releases(limit: int = 5) -> List:
    return [
               {'id': 'fastapi', 'summary': "A great web framework"},
               {'id': 'uvicorn', 'summary': "Your favorite ASGI server"},
               {'id': 'httpx', 'summary': "Requests for an async world"},
           ][:limit]


# {
#         'package_count': 274_000,
#         'release_count': 2_234_847,
#         'user_count': 73_874,
#         'packages': [
#             {'id': 'fastapi', 'summary': "A great web framework"},
#             {'id': 'uvicorn', 'summary': "Your favorite ASGI server"},
#             {'id': 'httpx', 'summary': "Requests for an async world"},
#         ]
#     }

def get_package_by_id(package_name: str) -> Optional[Package]:
    package = Package(
            package_name,
            "This is the summary",
            "Full details here!",
            "https://fastapi.tiangolo.com/",
            "MIT",
            "Sebastian Ramirez"
    )
    return package


def get_latest_release_for_package(package_name: str) -> Optional[Release]:
    return Release("1.2.0", datetime.datetime.now())

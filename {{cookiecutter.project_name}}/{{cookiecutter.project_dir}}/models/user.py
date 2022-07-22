from dataclasses import dataclass
from typing import Optional


@dataclass
class Name:
    title: str
    first: str
    last: str


@dataclass
class Result:
    gender: Optional[str]
    name: Name


@dataclass
class Info:
    seed: str
    results: int
    page: int
    version: str


@dataclass
class UserAPIResponse:
    results: list[Result]
    info: Optional[Info]

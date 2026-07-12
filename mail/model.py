from dataclasses import dataclass


@dataclass
class Mail:
    uid: int
    sender: str
    subject: str
    date: str

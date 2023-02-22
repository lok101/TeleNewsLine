from dataclasses import dataclass
from db.models import User, Channel


@dataclass
class ChannelData:
    id: int
    name: str

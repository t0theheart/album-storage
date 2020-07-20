from abc import ABC, abstractmethod


class AlbumsStorageABC(ABC):
    @classmethod
    @abstractmethod
    async def connect(cls, dsn: str): pass

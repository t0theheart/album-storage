from abc import ABC, abstractmethod


class AlbumsABC(ABC):
    @classmethod
    @abstractmethod
    async def start(cls): pass

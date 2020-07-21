from abc import ABC, abstractmethod


class AlbumsABC(ABC):
    @classmethod
    @abstractmethod
    async def start(cls): pass

    @abstractmethod
    async def create(self, data: dict): pass

    @abstractmethod
    async def get(self) -> list: pass

    @abstractmethod
    async def get_page(self) -> list: pass

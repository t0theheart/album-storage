from abc import ABC, abstractmethod


class AlbumsStorageABC(ABC):
    @classmethod
    @abstractmethod
    async def connect(cls, dsn: str): pass

    @abstractmethod
    async def create_album(self, title: str, author: str) -> int: pass

    @abstractmethod
    async def create_pages(self, album_id: int, pages: list): pass

    @abstractmethod
    async def get_albums(self) -> list: pass

    @abstractmethod
    async def get_page(self, album_id: int, page: int) -> dict: pass

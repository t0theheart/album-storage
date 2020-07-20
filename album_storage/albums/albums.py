from .abc import AlbumsABC
from album_storage.albums_storage import AlbumsStorage


class Albums(AlbumsABC):
    @classmethod
    async def start(cls):
        cls.storage = await AlbumsStorage.connect('postgresql://user:password@postgres:5433/albums')
        return cls()

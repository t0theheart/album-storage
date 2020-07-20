from .abc import AlbumsABC
from album_storage.albums_storage import AlbumsStorage


class Albums(AlbumsABC):
    @classmethod
    async def start(cls):
        cls.storage = await AlbumsStorage.connect('postgresql://user:password@postgres:5432/albums')
        return cls()

    async def create(self, data: dict):
        album_id = await self.storage.create_album(data['title'], data['author'])
        await self.storage.create_pages(album_id, data['pages'])
        return album_id

    async def get(self) -> list:
        return await self.storage.get_albums()

    async def get_page(self, album_id: int, page: int) -> dict:
        return await self.storage.get_page(album_id, page)

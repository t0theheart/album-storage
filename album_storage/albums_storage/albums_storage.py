from .abc import AlbumsStorageABC
import asyncpg


class AlbumsStorage(AlbumsStorageABC):
    @classmethod
    async def connect(cls, dsn: str):
        cls.pool = await asyncpg.create_pool(dsn=dsn)
        return cls()

from .abc import AlbumsStorageABC
import asyncpg


class AlbumsStorage(AlbumsStorageABC):
    @classmethod
    async def connect(cls, dsn: str):
        cls.pool = await asyncpg.create_pool(dsn=dsn)
        return cls()

    async def create_album(self, title: str, author: str) -> int:
        sql = f'''INSERT INTO "ALBUMS" ("TITLE", "AUTHOR") VALUES ('{title}', '{author}') RETURNING "ID"'''
        async with self.pool.acquire() as con:
            album_id = await con.fetchval(sql)
            return album_id

    async def create_pages(self, album_id: int, pages: list):
        sql = ''
        for n, page in enumerate(pages):
            sql += f'''
                INSERT INTO "PAGES" ("ALBUM_ID", "PAGE", "TEXT", "IMAGE") 
                VALUES ({album_id}, {n+1}, '{page['text']}', '{page['image']}');
            '''
        async with self.pool.acquire() as con:
            await con.execute(sql)

    async def get_albums(self) -> list:
        sql = f'''SELECT * FROM "ALBUMS"'''
        async with self.pool.acquire() as con:
            result = await con.fetch(sql)
            albums = [dict(album) for album in result]
            return albums

from aiohttp import web
from album_storage.api.views import routes
from album_storage.albums import Albums


async def create_app():
    app = web.Application()
    app.add_routes(routes)
    app['albums'] = await Albums.start()
    return app


if __name__ == '__main__':
    app = create_app()
    web.run_app(app, port=8081)

from aiohttp import web
from album_storage.api.serializers import AlbumCreateRequest, AlbumCreateResponse, AlbumsResponse


routes = web.RouteTableDef()


@routes.post('/albums')
async def login(request):
    data = AlbumCreateRequest().load(await request.json())
    album_id = await request.app['albums'].create(data)
    response = {'album_id': album_id}
    return web.json_response(
        data={'result': AlbumCreateResponse().dump(response)},
        headers={'Access-Control-Allow-Origin': '*'}
    )


@routes.get('/albums')
async def login(request):
    albums = await request.app['albums'].get()
    response = {'albums': albums}
    return web.json_response(
        data={'result': AlbumsResponse().dump(response)},
        headers={'Access-Control-Allow-Origin': '*'}
    )

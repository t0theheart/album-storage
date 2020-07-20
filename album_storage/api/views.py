from aiohttp import web
from album_storage.api.serializers import AlbumCreateRequest, AlbumCreateResponse


routes = web.RouteTableDef()


@routes.post('/albums/create')
async def login(request):
    data = AlbumCreateRequest().load(await request.json())
    album_id = await request.app['albums'].create(data)
    response = {'album_id': album_id}
    return web.json_response(
        data={'result': AlbumCreateResponse().dump(response)},
        headers={'Access-Control-Allow-Origin': '*'}
    )

from aiohttp import web


routes = web.RouteTableDef()


@routes.post('/test')
async def login(request):
    return web.json_response(
        data={'result': 123},
        headers={'Access-Control-Allow-Origin': '*'}
    )


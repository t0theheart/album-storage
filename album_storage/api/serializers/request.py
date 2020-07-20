from marshmallow import fields, Schema


class AlbumPage(Schema):
    text = fields.String(required=True, description='Text on page', example='My summer was ...')
    image = fields.String(required=True, description='Image source', example='https://www.example.com/image/1')


class AlbumCreateRequest(Schema):
    title = fields.String(required=True, description='Title', example='My summer 2020')
    author = fields.String(required=True, description='Author', example='Egor')
    pages = fields.List(fields.Nested(AlbumPage()), required=True, description='Pages of album')

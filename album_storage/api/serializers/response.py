from marshmallow import fields, Schema


class AlbumCreateResponse(Schema):
    albumId = fields.Integer(required=True, attribute='album_id', description='Album id', example='1')


class Album(Schema):
    title = fields.String(required=True, attribute='TITLE', description='Title', example='My summer 2020')
    author = fields.String(required=True, attribute='AUTHOR', description='Author', example='Egor')
    id = fields.Integer(required=True, attribute='ID', description='Album id', example='1')


class AlbumsResponse(Schema):
    albums = fields.List(fields.Nested(Album()), required=True, description='Albums')


class Page(Schema):
    text = fields.String(required=True, attribute='TEXT', description='Text', example='something...')
    image = fields.String(required=True, attribute='IMAGE', description='Image', example='https://www.example.com/image/1')
    number = fields.Integer(required=True, attribute='PAGE', description='Page number', example='1')


class PageResponse(Schema):
    page = fields.Nested(Page(), required=True, description='Page')

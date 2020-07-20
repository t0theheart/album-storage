from marshmallow import fields, Schema


class AlbumCreateResponse(Schema):
    albumId = fields.Integer(required=True, attribute='album_id', description='Album id', example='1')


class Album(Schema):
    title = fields.String(required=True, attribute='TITLE', description='Title', example='My summer 2020')
    author = fields.String(required=True, attribute='AUTHOR', description='Author', example='Egor')
    id = fields.Integer(required=True, attribute='ID', description='Album id', example='1')


class AlbumsResponse(Schema):
    albums = fields.List(fields.Nested(Album()), required=True, description='Albums')

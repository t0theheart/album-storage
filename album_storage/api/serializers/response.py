from marshmallow import fields, Schema


class AlbumCreateResponse(Schema):
    albumId = fields.Integer(required=True, attribute='album_id', description='Album id', example='1')

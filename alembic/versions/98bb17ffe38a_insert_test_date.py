"""insert test date

Revision ID: 98bb17ffe38a
Revises: 96fffd867679
Create Date: 2020-07-20 21:59:02.677157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98bb17ffe38a'
down_revision = '96fffd867679'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        INSERT INTO "ALBUMS" ("TITLE", "AUTHOR") VALUES ('My restaurants', 'mikebike'); 
        
        INSERT INTO "PAGES" ("ALBUM_ID", "PAGE", "TEXT", "IMAGE") 
        VALUES (1, 1, 'First restaurant', 'https://avatars.mds.yandex.net/get-pdb/472427/358db40f-008d-4719-ad76-b5cf841d5946/s1200?webp=false');
        
        INSERT INTO "PAGES" ("ALBUM_ID", "PAGE", "TEXT", "IMAGE") 
        VALUES (1, 2, 'Second restaurant', 'https://avatars.mds.yandex.net/get-pdb/1774156/4a93d345-3fcd-4ca8-94ca-c6999ecfc17b/s1200?webp=false');
        
        INSERT INTO "PAGES" ("ALBUM_ID", "PAGE", "TEXT", "IMAGE") 
        VALUES (1, 3, 'Third restaurant', 'https://million-wallpapers.ru/wallpapers/6/94/345483393497507/veneciya-nochyu.jpg');
        """
    )

    op.execute(
        """
        INSERT INTO "ALBUMS" ("TITLE", "AUTHOR") VALUES ('My pets', 'mikebike'); 

        INSERT INTO "PAGES" ("ALBUM_ID", "PAGE", "TEXT", "IMAGE") 
        VALUES (2, 1, 'First pet', 'https://get.pxhere.com/photo/grass-animal-pet-kitten-cat-feline-mammal-rest-fauna-friend-whiskers-animals-look-vertebrate-gata-norwegian-forest-cat-wild-cat-small-to-medium-sized-cats-cat-like-mammal-domestic-short-haired-cat-domestic-long-haired-cat-1383834.jpg');

        INSERT INTO "PAGES" ("ALBUM_ID", "PAGE", "TEXT", "IMAGE") 
        VALUES (2, 2, 'Second pet', 'https://im0-tub-ru.yandex.net/i?id=d5e436bd83e80a4c5f9e3ff755b43bb5&n=13');

        INSERT INTO "PAGES" ("ALBUM_ID", "PAGE", "TEXT", "IMAGE") 
        VALUES (2, 3, 'Third pet', 'https://im0-tub-ru.yandex.net/i?id=5c0e94e08e7287d3c0e35c370dab5a36&n=13');
        """
    )

    op.execute(
        """
        INSERT INTO "ALBUMS" ("TITLE", "AUTHOR") VALUES ('Robots', 'Alex123'); 

        INSERT INTO "PAGES" ("ALBUM_ID", "PAGE", "TEXT", "IMAGE") 
        VALUES (3, 1, 'First robot, it is very smart amd powerful. It protects people from aliens!', 'https://avatars.mds.yandex.net/get-pdb/2028552/407612e3-32a7-484f-ba64-30cf57a764f4/s1200?webp=false');

        INSERT INTO "PAGES" ("ALBUM_ID", "PAGE", "TEXT", "IMAGE") 
        VALUES (3, 2, 'Second robot, it looks like a cat, but it does not like milk', 'https://im0-tub-ru.yandex.net/i?id=502455ff6b6f4b0af066279b47cf3f3e&n=13');

        INSERT INTO "PAGES" ("ALBUM_ID", "PAGE", "TEXT", "IMAGE") 
        VALUES (3, 3, 'Third robot, it is support. It can clear your house or wash dishes', 'https://i.pinimg.com/736x/6d/76/cb/6d76cb60510ba5dab5fa94cf226abeed.jpg');
        
        INSERT INTO "PAGES" ("ALBUM_ID", "PAGE", "TEXT", "IMAGE") 
        VALUES (3, 4, 'Fourth robot. It is the biggest. Information about this robot should keep in secret', 'https://kartinkinaden.ru/uploads/posts/2019-08/1566270225_art-robot-54.jpg');
        """
    )


def downgrade():
    op.execute('TRUNCATE TABLE "ALBUMS"')
    op.execute('TRUNCATE TABLE "PAGES"')

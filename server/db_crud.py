import asyncio

from sqlalchemy.orm import Session
from server import models
from server.elastic import Elastic

from asgiref.wsgi import WsgiToAsgi

elastic = Elastic()


def delete_post_by_id(id_delete: int):
    deleted_post = elastic.search_by_id(id_delete)

    if deleted_post is not None:
        elastic_deleted = elastic.delete_by_id(deleted_post[0]['_id'])

        return elastic_deleted
    return False


def get_posts(db: Session, text: str):
    id_list = [item["id"] for item in elastic.search_by_text(text)]

    result =db.query(models.Post) \
        .filter(models.Post.id.in_(id_list)) \
        .order_by(models.Post.created_date.desc()) \
        .all()
    return result

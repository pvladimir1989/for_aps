# from flask import request

from quart import Quart, g, request
from quart.helpers import make_response

from server import app, db_crud
from sqlalchemy.orm import Session
from server.database_settings import SessionLocal


@app.route('/get_posts', methods=['GET'])
async def get_posts():
    db: Session = SessionLocal()

    try:
        query = request.args.get('query', default='')
        results_posts_list = await db_crud.get_posts(db=db, text=query)
        return {'result': [x.get_data() for x in results_posts_list]}
    except Exception as exc:
        return str(exc)


@app.route('/delete_post', methods=['GET', 'DELETE'])
def delete_post():
    try:
        id = int(request.args.get('id', default=''))
        db_crud.delete_post_by_id(id_delete=id)
        return {'deleted': id}
    except Exception as exc:
        return str(exc)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)

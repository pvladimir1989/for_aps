from flask import request
from quart import Quart, g, request
from json import dumps
import asyncio
from server import app, db_crud
from sqlalchemy.orm import Session
from server.database_settings import SessionLocal

# loop = asyncio.get_event_loop()
# asyncio.set_event_loop(loop)


# def get_thread_event_loop():
#     try:
#         loop = asyncio.get_event_loop()  # gets previously set event loop, if possible
#     except RuntimeError:
#         loop = asyncio.new_event_loop()
#         asyncio.set_event_loop(loop)
#     return loop


@app.route('/get_posts', methods=['GET'])
def get_posts():
    db: Session = SessionLocal()
    print(db)
    # loop: get_thread_event_loop()
    # loop = asyncio.get_event_loop()
    # asyncio.set_event_loop(loop)
    try:
        query = request.args.get('query', default='')
        print(query)
        results_posts_list = db_crud.get_posts(db=db, text=query)
        return {'result': dumps([x.get_data() for x in results_posts_list])}
    except Exception as exc:
        print(exc)
        return str(exc)


@app.route('/delete_post', methods=['GET', 'DELETE'])
def delete_post():
    try:
        id = int(request.args.get('id', default=''))
        db_crud.delete_post_by_id(id_delete=id)
        return {'deleted': id}
    except Exception as exc:
        return str(exc)


# loop = asyncio.get_event_loop()
# loop.run_until_complete(get_posts())


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)

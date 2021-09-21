from flask import request

from server import app, db_crud

from sqlalchemy.orm import Session

from server.database_settings import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/get_posts', methods=['GET'])
def get_posts(db: Session = get_db):  # put application's code here
    try:
        query = request.args["query"]
        results_posts_list = db_crud.get_posts(db=db, text=query)
        return {"result": results_posts_list}
    except Exception as exc:
        return str(exc)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

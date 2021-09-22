from flask import request

from server import app, db_crud

from sqlalchemy.orm import Session,sessionmaker

from server.database_settings import SessionLocal, engine

# import models

# session = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    print(db)
    try:
        yield db
    finally:
        db.close()


@app.route('/')
def hello_world(b="dfgdgf"):  # put application's code here
    return b


@app.route('/get_posts', methods=['GET'])
def get_posts():
    db: Session = SessionLocal()

    print(db,"sdgfdsfgdsfgdsfg")
    try:
        query = request.args.get("query")
        print(db)
        print(query)
        results_posts_list = db_crud.get_posts(db=db, text=query)
        # print(results_posts_list)
        return {"result": results_posts_list}
    except Exception as exc:
        print("dsfgdfsgdsfgdfgsdfg", exc)
        return str(exc)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)

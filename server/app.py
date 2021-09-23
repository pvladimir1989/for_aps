from flask import request
from server import app, db_crud
from sqlalchemy.orm import Session
from server.database_settings import SessionLocal
from pydantic import BaseModel


class DeletePost(BaseModel):
    id: int

    class Config:
        orm_mode = True


@app.route('/get_posts', methods=['GET'])
def get_posts():
    db: Session = SessionLocal()
    try:
        query = request.args.get("query")
        results_posts_list = db_crud.get_posts(db=db, text=query)
        return {"result": results_posts_list}
    except Exception as exc:
        return str(exc)


@app.route("/delete_post", methods=["DELETE"])
def delete_post():
    post: DeletePost
    db: Session = SessionLocal()
    print(db)
    try:
        # id = int(request.args.get["id"])
        # print(id)
        result = db_crud.delete_post_by_id(db=db, id_delete=DeletePost.id)
        return {"deleted": result}
    except Exception as exc:
        return str(exc)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)

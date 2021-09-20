from server import db


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rubrics = db.Column(db.ARRAY(db.Text()), nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Post {}>'.format(self.rubrics)

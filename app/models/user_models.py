from app import db


class MinifiedUrl(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    url = db.Column('url', db.String(155), unique=True, nullable=False)
    ttl = db.Column('ttl', db.Integer, nullable=True)

    def __repr__(self):
        return '<id=%r, url=%r, ttl=%r'.format(self.id, self.url, self.ttl)

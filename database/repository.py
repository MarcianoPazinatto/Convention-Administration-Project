from database import db

_session = db.session


def save(model: db.Model):
    _session.add(model)
    commit()
    return model


def delete(model: db.Model):
    _session.delete(model)
    commit()
    return model


def update(model: db.Model):
    _session.query


def commit():
    _session.commit()

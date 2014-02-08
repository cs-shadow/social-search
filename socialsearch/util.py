import time

def getTimeEpoch():
    return int(time.mktime(time.gmtime()))

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = getattr(row, column.name)

    return d
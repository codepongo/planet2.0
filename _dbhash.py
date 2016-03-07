import dbm
class _dbm(object):
    def __init__(self, dbm):
        self.dbm = dbm
    def has_key(self, k):
        return self.dbm.has_key(k)
    def keys(self):
        return self.dbm.keys()
    def sync(self):
        pass
    def __getitem__(self, k):
        return self.dbm[k]
    def __setitem__(self, k, v):
        self.dbm[k] = v
def open(filename, flag, mode):
    return _dbm(dbm.open(filename, flag, mode))


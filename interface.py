class DBDB(object):
    def __init__(self,f):
        self._storage=Storage(f)#so basically storage is another function which we input file object f
        self._tree=Bin(self._storage)#here the line basically is self._tree=BinaryTree(Storage(f))
    def getitem(self,key):
        self._assert_not_closed()
        return self._tree.get(key)
    def _assert_not_closed(self):
        if self._storage.closed:
            raise ValueError('Database closed.')    

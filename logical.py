import portalocker
class logicalbase(object):
    def set(self, key, value):
        if self._storage.lock():
            self._refresh_tree_ref()
        self._tree_ref=self.insert(
                self.follow(self._tree_ref), key, self.value_ref_class(value))
class ValueRef(object):
    def store(self, storage):
        if self.referent is not None and not self._address:
            self.prepare_to_store(storage)
            self.address=storage.write(self.referent_to_string(self.referent))
    def store(self, storage):
        if self._referent is not None and not self._address:
            self.prepare_to_store(storage)
            self._address=storage.write(self.referent_to_string(self._referent))

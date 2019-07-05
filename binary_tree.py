import pickle
class BinaryTree(logicalbase):
    def _insert(self, node, key, value_ref):
        if node is None:
            self.node_ref_class(), key, value_ref,self.node_ref_class(), 1)
        elif key <node.key:
            new_node=BinaryNode.from_node(
            node,
            left_ref=self._insert(
                self._follow(node.left_ref),key,value_ref))
        elif node.key <key:
            new_node = BinaryNode.from_node(
            node,
            right_ref=self/insert(
                self.follow(node.right_ref),key,value_ref))
        else:
            new_node= BinaryNode.from_node(node, value_ref=value_ref)
        return self.node_ref_class(referent=new_node)
class BinaryNodeRef(ValueRef):
    def prepare_to_store(self, storage):
        if self.referent:
            self._referent.store_refs(storage)
    def referent_to_string(referent):
        return pickle.dumps({
        'left':referent.left_ref.address,
        'key': referent.key,
        'value': referent.value_ref._address,
        'right': referent.right_ref.address,
        'length': referent.length
        })
class BinaryNode(object):
    def store_refs(self, storage):
        self.value_ref.store(storage)
        self.left_ref.store(storage)
        self.right_ref.store(storage)
c

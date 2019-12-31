from pymerkles.core import View
from pymerkles.tree import Root, merkle_hash


def serialize(obj: View) -> bytes:
    return obj.encode_bytes()


def hash_tree_root(obj: View) -> Root:
    return obj.get_backing().merkle_root(merkle_hash)

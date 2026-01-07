import hashlib

def hashed_feature(value: str, num_buckets: int = 10) -> int:
    """Verilen string'i hashleyip bucket index'i döndürür."""
    hash_object = hashlib.md5(value.encode())
    hash_int = int(hash_object.hexdigest(), 16)
    return hash_int % num_buckets
<<<<<<< HEAD
=======

>>>>>>> 979664cf39526b543a0f9e2c4974a5188be48d3a

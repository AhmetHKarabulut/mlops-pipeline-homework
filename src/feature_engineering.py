# feature_engineering.py

def hash_feature(value: str, num_buckets: int = 10) -> int:
    """Simple hashing function to map string to a bucket index"""
    return hash(value) % num_buckets

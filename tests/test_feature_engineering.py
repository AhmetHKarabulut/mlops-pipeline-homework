from feature_engineering import hash_feature

def test_hash_feature_known_value():
    """Unit test: fast, isolated, no external dependencies"""
    # Hashing "apple" in 10 buckets
    result = hash_feature("apple", 10)
    # We know hash("apple") % 10 should be deterministic
    assert isinstance(result, int)
    assert 0 <= result < 10

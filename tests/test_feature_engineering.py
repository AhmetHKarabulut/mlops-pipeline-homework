from src.feature_engineering import hashed_feature

def test_hashed_feature_known_value():
    assert hashed_feature("apple", 10) == hashed_feature("apple", 10)
    assert hashed_feature("mlops", 10) == hashed_feature("mlops", 10)

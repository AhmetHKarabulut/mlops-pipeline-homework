from src.feature_engineering import hashed_feature

def test_hashed_feature_known_value():
    assert hashed_feature("apple", 10) == 4  # bilinen input için beklenen bucket
    assert hashed_feature("banana", 10) == 6


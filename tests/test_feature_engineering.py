from src.feature_engineering import FeatureHasher

def test_hashed_feature_known_value():
<<<<<<< HEAD
    assert hashed_feature("apple", 10) == hashed_feature("apple", 10)
    assert hashed_feature("mlops", 10) == hashed_feature("mlops", 10)
=======
    assert hashed_feature("apple", 10) == 4  # bilinen input için beklenen bucket
    assert hashed_feature("banana", 10) == 6

>>>>>>> 979664cf39526b543a0f9e2c4974a5188be48d3a

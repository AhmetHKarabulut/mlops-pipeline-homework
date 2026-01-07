import pytest
from src.feature_engineering import hash_features

def test_hash_features_output_type():
    data = [{"text": "mlops pipeline"}]
    result = hash_features(data, "text")
    assert isinstance(result, list)

def test_hash_features_not_empty():
    data = [{"text": "mlops"}]
    result = hash_features(data, "text")
    assert len(result) > 0

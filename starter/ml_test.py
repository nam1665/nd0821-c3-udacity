"""
Unit test for ML model
"""
import pandas as pd
import pytest
import joblib
import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from training.ml.data import process_data

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

# Utilizing a fixture facilitates the reuse of data by storing it in a variable, in this case, a Pandas DataFrame.
@pytest.fixture()
def data():
    # Check if the path and file exists
    assert os.path.exists('starter/data/clean_census.csv')
    return pd.read_csv('starter/data/clean_census.csv')


def test_data_and_features(data):
    # Data should greater than 100 samples
    assert data.shape[0] > 100

    # Data should equal 15 features
    assert data.shape[1] == 15

    # Confirm that all categorical features are present in the provided data.
    for cat_feat in cat_features:
        assert cat_feat in list(data.columns)


def test_process_data_function(data):
    train, test = train_test_split(data, random_state=42, test_size=0.2)
    X, y, _, _ = process_data(
        train, cat_features, label='salary'
    )
    assert len(X) == len(y)


def test_model_and_paths():
    # Verify the existence of all the model files.
    assert os.path.exists("starter/model/rf_model.pkl")
    assert os.path.exists("starter/model/encoder.pkl")
    assert os.path.exists("starter/model/lb.pkl")

    # Load model
    model = joblib.load("starter/model/rf_model.pkl")
    assert isinstance(model, RandomForestClassifier)

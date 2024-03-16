import pandas as pd
import numpy as np
from DataPrepKit.missing_values import drop_missing_values, fill_missing_values
from DataPrepKit.categorical_encoding import encode_categorical
from DataPrepKit.outliers import detect_outliers
from DataPrepKit.normalization import normalize_data

def test_drop_missing_values():
    data = pd.DataFrame({
        'A': [1, 2, np.nan, 4],
        'B': [5, np.nan, 7, 8],
        'C': ['a', 'b', 'c', 'd']
    })
    expected_output = pd.DataFrame({
        'A': [1.0, 2.0, 4.0],
        'B': [5.0, 7.0, 8.0],
        'C': ['a', 'b', 'd']
    }, index=[0, 1, 3])
    assert drop_missing_values(data).equals(expected_output)

def test_fill_missing_values():
    data = pd.DataFrame({
        'A': [1, 2, np.nan, 4],
        'B': [5, np.nan, 7, 8],
        'C': ['a', 'b', 'c', 'd']
    })
    expected_output = pd.DataFrame({
        'A': [1.0, 2.0, 3.0, 4.0],
        'B': [5.0, 6.0, 7.0, 8.0],
        'C': ['a', 'b', 'c', 'd']
    })
    assert fill_missing_values(data, method='mean').equals(expected_output)

def test_encode_categorical():
    data = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': ['a', 'b', 'a', 'b'],
        'C': ['x', 'y', 'x', 'y']
    })
    expected_output = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B_a': [1, 0, 1, 0],
        'B_b': [0, 1, 0, 1],
        'C': ['x', 'y', 'x', 'y']
    })
    assert encode_categorical(data, column='B', method='one-hot').equals(expected_output)

def test_detect_outliers():
    data = pd.DataFrame({
        'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100],
        'B': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1000]
    })
    expected_output = pd.DataFrame({
        'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'B': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    })
    assert detect_outliers(data, method='zscore', threshold=3).equals(expected_output)

def test_normalize_data():
    data = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]
    })
    expected_output = pd.DataFrame({
        'A': [0.0, 0.25, 0.5, 0.75, 1.0],
        'B': [0.0, 0.25, 0.5, 0.75, 1.0]
    })
    assert normalize_data(data).equals(expected_output)

if __name__ == "__main__":
  test_drop_missing_values()
  test_fill_missing_values()
  test_encode_categorical()
  test_detect_outliers()
  test_normalize_data()

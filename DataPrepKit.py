import pandas as pd
import numpy as np

class DataPrepKit:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)

    def read_data(self, file_path, file_format='csv'):
        file_extension = file_path.split(".")[-1]
        if file_extension == 'csv':
            self.data = pd.read_csv(file_path)
        elif file_extension == 'excel':
            self.data = pd.read_excel(file_path)
        elif file_extension == 'json':
            self.data = pd.read_json(file_path)
        else:
            raise ValueError("Unsupported file format")

    def data_summary(self):
        summary = self.data.describe()
        return summary

    def handle_missing_values(self, strategy='remove'):
        if strategy == 'remove':
            self.data.dropna(inplace=True)
        elif strategy == 'impute_mean':
            self.data.fillna(self.data.mean(), inplace=True)
        elif strategy == 'impute_median':
            self.data.fillna(self.data.median(), inplace=True)
        else:
            raise ValueError("Invalid missing value handling strategy")

    def encode_categorical_data(self, columns):
        encoded_data = pd.get_dummies(self.data, columns=columns)
        return encoded_data

    def save_processed_data(self, file_path):
        self.data.to_csv(file_path, index=False)

# Example Usage:
if __name__ == "__main__":
    data_prep = DataPrepKit("data.csv")

    data_prep.read_data("data.xlsx", file_format='excel')
    data_prep.read_data("data.json", file_format='json')

    summary = data_prep.data_summary()

    data_prep.handle_missing_values(strategy='remove')

    encoded_data = data_prep.encode_categorical_data(columns=['category_column'])

    data_prep.save_processed_data("processed_data.csv")

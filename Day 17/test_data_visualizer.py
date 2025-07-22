import unittest
import os
import pandas as pd
from data_visualizer import load_data, preprocess_data, generate_plots, DatasetNotFoundError

class TestEDATool(unittest.TestCase):
    def setUp(self):
        self.test_file = 'Sales Dataset.csv'
        self.df = load_data(self.test_file)

    def test_load_data_valid(self):
        self.assertIsInstance(self.df, pd.DataFrame)
        self.assertFalse(self.df.empty)

    def test_load_data_invalid(self):
        with self.assertRaises(DatasetNotFoundError):
            load_data("non_existing_file.csv")

    def test_preprocess_data(self):
        df_processed = preprocess_data(self.df.copy())
        self.assertIn("Year-Month", df_processed.columns)
        self.assertTrue(pd.api.types.is_string_dtype(df_processed['Year-Month']))

    def test_generate_plots(self):
        df_processed = preprocess_data(self.df.copy())
        generate_plots(df_processed)
        self.assertTrue(os.path.exists("plots/Line Chart.png"))
        self.assertTrue(os.path.exists("plots/Bar Chart.png"))
        self.assertTrue(os.path.exists("plots/Pie Chart.png"))
        self.assertTrue(os.path.exists("plots/Heatmap.png"))

    def tearDown(self):
        pass  # Clean-up if needed

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)



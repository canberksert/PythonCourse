import unittest
import pandas as pd
import hw2_30223_oguzhan_akan_regression as h


class RegressionTest(unittest.TestCase):

    # test for reading the data
    def test__read_data(self):
        df = h.read_data(path='hw2_30223_oguzhan_akan_data.csv',target='target_birth_rate')
        self.assertEqual(type(df),type(pd.DataFrame()))
        
    # test for the regression function    
    def test__findEstimates(self):
        path='hw2_30223_oguzhan_akan_data.csv'
        target='birth_rate'
        df = h.read_data(path,target)
        df = h.handle_na(df)
        regression_table, y, y_hat = h.findEstimates(df,target,alpha=0.05)
        self.assertNotEqual(len(regression_table.index),len(df.columns))

if __name__ == '__main__':
    unittest.main()
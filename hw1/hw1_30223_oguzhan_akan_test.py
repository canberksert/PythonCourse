
# coding: utf-8

# In[ ]:
import unittest
import hw1_30223_oguzhan_akan as h


class PortfolioTest(unittest.TestCase):

    def test_addCash(self):
        a = h.Portfolio()
        a.addCash(50)
        self.assertEqual(a.cash,50)

    def test_Stock_MF(self):
        s = h.Stock(50,'HFH')
        self.assertEqual(s.price,50)
        self.assertEqual(s.symbol,'HFH')
        mf1 = h.MutualFund(symbol='BRT')
        self.assertEqual(mf1.price,1)
        self.assertEqual(mf1.symbol,'BRT')

    def test_buyStock(self):
        a = h.Portfolio(initialCash = 1000)
        s = h.Stock(50,'HFH')
        a.buyStock(2,s)
        self.assertTrue(len(a.stocks)>0)

if __name__ == '__main__':
    unittest.main()

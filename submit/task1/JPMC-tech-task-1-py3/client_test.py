import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]   
    for quote in quotes:
        self.assertEqual(getDataPoint(quote),(quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price']+ quote['top_ask']['price'])/2))
  
  
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
        self.assertEqual(getDataPoint(quote),(quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price']+ quote['top_ask']['price'])/2))

  """ ------------ Add more unit tests ------------ """
  
  def test_getRatio(self):
      data = [
        {'abc_price' : 114.25, 'def_price' : 112.035 , 'ratio' : 1.0197706073994734},
        {'abc_price' : 117.38, 'def_price' : 116.325 , 'ratio' : 1.0090694175800559},
        {'abc_price' : 117.38, 'def_price' : 0 , 'ratio' : None}
      ]
      for val in data:
            self.assertEqual(getRatio(val['abc_price'],val['def_price']),val['ratio'])
      



if __name__ == '__main__':
    unittest.main()

import unittest
#from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.Testcase):
    def setUp(self):
        self.kassapaate = Kassapaate()
    
    def test_alkuraha_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
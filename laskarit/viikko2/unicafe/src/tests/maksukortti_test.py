import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_alkusaldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataus_toimii(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 11.00 euroa")

    def test_rahan_otto_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(800)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 2.00 euroa")
    
    def test_rahan_otto_ei_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(1200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_metodi_palauttaa_true_jos_onnistui(self):
        self.assertEqual(self.maksukortti.ota_rahaa(800), True)
    
    def test_metodi_palauttaa_false_jos_epaonnistui(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1200), False)

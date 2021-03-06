import sys
sys.path.append('../')
import unittest
from wormbase_parasite import WormbaseClient
import test_util

class TestCrossReferenceMethods(unittest.TestCase):
    def setUp(self):
        self.api = WormbaseClient()

    def doTest(self, response):
        self.assertTrue(type(response) is list)

    def test_xrefs_for_symbol(self):
        self.doTest(self.api.get_xrefs_for_symbol(
            'brugia_malayi_prjna10729', 'Bm994'))

    def test_xrefs_for_id(self):
        self.doTest(self.api.get_xrefs_for_id('WBGene00221255'))

    def test_xrefs_for_gene_and_species(self):
        self.doTest(self.api.get_xrefs_for_gene_and_species(
            'Bm994', 'brugia_malayi_prjna10729'))

if __name__ == '__main__':
    unittest.main()

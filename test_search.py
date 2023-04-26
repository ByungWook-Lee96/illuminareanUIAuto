import time
from unittest import TestCase
import search


class Test(TestCase):
    def test_001(self):
        search.search_stock()
        time.sleep(3)

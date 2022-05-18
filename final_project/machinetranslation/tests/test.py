import unittest
from translator import french_to_english
from translator import english_to_french

class TestMyModule(unittest.TestCase):
    def test_f2e(self):
        self.assertEqual(french_to_english('comment es-tu aujourd\'hui?'),'How are you today?')
    def test_f2e1(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
    def test_f2e2(self):
        self.assertNotEqual(french_to_english('None'),'')
    def test_f2e3(self):
        self.assertNotEqual(french_to_english(0),0)

class TestMyModule1(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(english_to_french('How are you today?'),'Comment es-tu aujourd\'hui?')
    def test_e2f1(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
    def test_e2f2(self):
        self.assertNotEqual(english_to_french('None'),'')
    def test_e2f3(self):
        self.assertNotEqual(english_to_french(0),0)

unittest.main()
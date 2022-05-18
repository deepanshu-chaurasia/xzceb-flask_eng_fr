import unittest
from translator import frenchToEnglish
from translator import englishToFrench

class TestMyModule(unittest.TestCase):
    def test_f2e(self):
        self.assertEqual(frenchToEnglish('comment es-tu aujourd\'hui?'),'How are you today?')
    def test_f2e1(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
    def test_f2e2(self):
        self.assertNotEqual(frenchToEnglish('None'),'')
    def test_f2e3(self):
        self.assertNotEqual(frenchToEnglish(0),0)

class TestMyModule1(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(englishToFrench('How are you today?'),'Comment es-tu aujourd\'hui?')
    def test_e2f1(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
    def test_e2f2(self):
        self.assertNotEqual(englishToFrench('None'),'')
    def test_e2f3(self):
        self.assertNotEqual(englishToFrench(0),0)

unittest.main()
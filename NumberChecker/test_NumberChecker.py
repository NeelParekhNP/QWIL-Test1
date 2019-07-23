import unittest
import NumberChecker

class TestNumberChecker(unittest.TestCase):
    
    def test_myFunction(self):
        self.assertEqual(NumberChecker.myFunction("0200"), "1001")
        self.assertEqual(NumberChecker.myFunction("-1"), "-1")
        self.assertEqual(NumberChecker.myFunction("0"), "-1")
        self.assertEqual(NumberChecker.myFunction("01"), "10")
        self.assertEqual(NumberChecker.myFunction("123"), "132")
        self.assertEqual(NumberChecker.myFunction("90"), "-1")
        self.assertEqual(NumberChecker.myFunction("9999"), "-1")
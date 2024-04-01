import unittest
import numpy as np
from src import PolyCurveFitting

class TestPolynomial(unittest.TestCase):
    def setUp(self):
        self.dataset = np.linspace(0,10,1,endpoint=False)
        self.coeff_vector = np.array([1,2,3])

        self.poly_object = PolyCurveFitting(self.coeff_vector,self.dataset)
    
    def testPolyVal(self):
        self.assertEqual(self.poly_object.PolyVal(1), 6, "Should be 1 + 2*(x^1) + 3*(x^2)")
    
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
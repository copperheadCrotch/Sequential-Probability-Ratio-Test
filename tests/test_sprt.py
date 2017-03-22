from unittest import TestCase
import sprt

class TestSPRTNormal(TestCase):

    def test_sprt_result(self):

        values = [-0.33, 0.64, -0.35, 1.23, -0.98, 0.05]
        result = sprt.SPRTNormal(alpha = 0.05, beta = 0.2, values = values)
        self.assertEqual(result, 'Accept')

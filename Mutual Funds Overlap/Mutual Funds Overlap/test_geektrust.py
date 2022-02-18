import unittest
from geektrust import main
import sys

class TestStringMethods(unittest.TestCase):

    def test_one(self):
        expected_output = [['MIRAE_ASSET_EMERGING_BLUECHIP AXIS_BLUECHIP 39.13%', 'MIRAE_ASSET_EMERGING_BLUECHIP ICICI_PRU_BLUECHIP 38.10%', 'MIRAE_ASSET_EMERGING_BLUECHIP UTI_NIFTY_INDEX 65.52%'], ['MIRAE_ASSET_LARGE_CAP AXIS_BLUECHIP 43.75%', 'MIRAE_ASSET_LARGE_CAP ICICI_PRU_BLUECHIP 44.62%', 'MIRAE_ASSET_LARGE_CAP UTI_NIFTY_INDEX 95.00%'], ['MIRAE_ASSET_EMERGING_BLUECHIP AXIS_BLUECHIP 38.71%', 'MIRAE_ASSET_EMERGING_BLUECHIP ICICI_PRU_BLUECHIP 38.10%', 'MIRAE_ASSET_EMERGING_BLUECHIP UTI_NIFTY_INDEX 65.52%']]
        self.assertEqual(main("instructions1.txt"), expected_output)

    def test_two(self):
        expected_output = [['AXIS_MIDCAP ICICI_PRU_NIFTY_NEXT_50_INDEX 14.81%', 'AXIS_MIDCAP PARAG_PARIKH_CONSERVATIVE_HYBRID 93.44%', 'AXIS_MIDCAP ICICI_PRU_BLUECHIP 14.52%'], ['SBI_LARGE_&_MIDCAP PARAG_PARIKH_CONSERVATIVE_HYBRID 8.47%']]
        self.assertEqual(main("instructions2.txt"), expected_output)

    def test_three(self):
        expected_output = [['ICICI_PRU_NIFTY_NEXT_50_INDEX UTI_NIFTY_INDEX 20.37%', 'ICICI_PRU_NIFTY_NEXT_50_INDEX AXIS_MIDCAP 14.81%', 'ICICI_PRU_NIFTY_NEXT_50_INDEX PARAG_PARIKH_FLEXI_CAP 7.41%'], ['ICICI_PRU_NIFTY_NEXT_50_INDEX UTI_NIFTY_INDEX 20.37%', 'ICICI_PRU_NIFTY_NEXT_50_INDEX AXIS_MIDCAP 14.68%', 'ICICI_PRU_NIFTY_NEXT_50_INDEX PARAG_PARIKH_FLEXI_CAP 7.32%']]
        self.assertEqual(main("instructions3.txt"), expected_output)

    def test_four(self):
        expected_output = [['ICICI_PRU_BLUECHIP ICICI_PRU_NIFTY_NEXT_50_INDEX 25.42%', 'ICICI_PRU_BLUECHIP AXIS_BLUECHIP 44.00%', 'ICICI_PRU_BLUECHIP AXIS_MIDCAP 14.52%'], ['ICICI_PRU_BLUECHIP ICICI_PRU_NIFTY_NEXT_50_INDEX 26.89%', 'ICICI_PRU_BLUECHIP AXIS_BLUECHIP 44.00%', 'ICICI_PRU_BLUECHIP AXIS_MIDCAP 14.52%']]
        self.assertEqual(main("instructions4.txt"), expected_output)


if __name__ == '__main__':
    unittest.main()
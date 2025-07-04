import unittest
from sea_level_predictor import draw_plot

class TestSeaLevelPredictor(unittest.TestCase):
    def test_plot_exists(self):
        fig = draw_plot()
        self.assertIsNotNone(fig)

if _name_ == '_main_':
    unittest.main()

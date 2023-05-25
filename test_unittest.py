#Драгунова Анастасия Евгеньевна Группа 44-22-115 Вариант 6 Задание 2
import unittest
import numpy as np
from func import func 
test = []
class TestCalculate(unittest.TestCase):
    def test_1(self):
        self.assertEqual(func(4),float(np.sin(1/4)))

    
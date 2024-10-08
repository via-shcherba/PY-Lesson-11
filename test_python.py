import unittest
import math

class TestBuiltInFunctions(unittest.TestCase):

    def test_filter(self):
        # Тест фильтрации четных чисел
        result = list(filter(lambda x: x % 2 == 0, range(10)))
        self.assertEqual(result, [0, 2, 4, 6, 8])
        
        # Тест фильтрации чисел больше 5
        result = list(filter(lambda x: x > 5, range(10)))
        self.assertEqual(result, [6, 7, 8, 9])
        
        # Тест фильтрации строк
        result = list(filter(lambda x: isinstance(x, str), [1, 'a', 2, 'b', 3]))
        self.assertEqual(result, ['a', 'b'])
        
        # Тест фильтрации пустого списка
        result = list(filter(lambda x: x > 0, []))
        self.assertEqual(result, [])
        
        # Тест фильтрации с None
        result = list(filter(None, [0, '', None, 1, 'abc']))
        self.assertEqual(result, [1, 'abc'])

    def test_map(self):
        # Тест возведения в квадрат
        result = list(map(lambda x: x ** 2, range(5)))
        self.assertEqual(result, [0, 1, 4, 9, 16])
        
        # Тест объединения строк
        result = list(map(str, range(3)))
        self.assertEqual(result, ['0', '1', '2'])
        
        # Тест сложения двух списков
        result = list(map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6]))
        self.assertEqual(result, [5, 7, 9])
        
        # Тест пустого списка
        result = list(map(lambda x: x * 2, []))
        self.assertEqual(result, [])
        
        # Тест преобразования в верхний регистр
        result = list(map(str.upper, ['a', 'b', 'c']))
        self.assertEqual(result, ['A', 'B', 'C'])

    def test_sorted(self):
        # Тест сортировки списка чисел
        result = sorted([5, 2, 9, 1, 5, 6])
        self.assertEqual(result, [1, 2, 5, 5, 6, 9])
        
        # Тест сортировки списка строк
        result = sorted(['banana', 'apple', 'cherry'])
        self.assertEqual(result, ['apple', 'banana', 'cherry'])
        
        # Тест сортировки с обратным порядком
        result = sorted([5, 2, 9, 1, 5, 6], reverse=True)
        self.assertEqual(result, [9, 6, 5, 5, 2, 1])
                
        # Тест сортировки по длине строк
        result = sorted(['a', 'abc', 'ab'], key=len)
        self.assertEqual(result, ['a', 'ab', 'abc'])

class TestMathFunctions(unittest.TestCase):

    def test_pi(self):
        self.assertAlmostEqual(math.pi, 3.141592653589793, places=7)

    def test_sqrt(self):
        # Тест квадратного корня
        self.assertEqual(math.sqrt(4), 2)
        self.assertEqual(math.sqrt(0), 0)
        self.assertAlmostEqual(math.sqrt(2), 1.4142135623730951, places=7)
        with self.assertRaises(ValueError):
            math.sqrt(-1)

    def test_pow(self):
        # Тест возведения в степень
        self.assertEqual(math.pow(2, 3), 8)
        self.assertEqual(math.pow(9, 0.5), 3)
        self.assertEqual(math.pow(5, -1), 0.2)

    def test_hypot(self):
        # Тест расчета гипотенузы
        self.assertEqual(math.hypot(3, 4), 5)
        self.assertEqual(math.hypot(0, 0), 0)
        self.assertAlmostEqual(math.hypot(1, 1), math.sqrt(2), places=7)

if __name__ == '__main__':
    unittest.main()
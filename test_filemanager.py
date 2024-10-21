import unittest
from unittest.mock import patch
from io import StringIO
from file_operations import *
from bank_account import *
from quiz import *
from system_info import *

class TestFileOperations(unittest.TestCase):
    
    def setUp(self):
        # Сброс глобальных переменных перед каждым тестом
        global balance, purchase_history
        balance = 0.0
        purchase_history = []

    @patch('os.makedirs')
    @patch('builtins.input', side_effect=['test_folder'])
    def test_create_folder(self, mock_input, mock_makedirs):
        create_folder()
        mock_makedirs.assert_called_once_with('test_folder', exist_ok=True)

    @patch('os.rmdir')
    @patch('os.remove')
    @patch('builtins.input', side_effect=['test_file'])
    def test_delete_file(self, mock_input, mock_remove, mock_rmdir):
        delete_item()
        mock_remove.assert_called_once_with('test_file')

    @patch('os.rmdir')
    @patch('os.remove')
    @patch('shutil.copytree')
    @patch('shutil.copy')
    @patch('builtins.input', side_effect=['main.py', 'main2.py'])
    def test_copy_file(self, mock_input, mock_copy, mock_copytree, mock_remove, mock_rmdir):
        # Тестируем копирование файла
        copy_item()
        mock_copy.assert_called_once_with('main.py', 'main2.py')

        # Тестируем копирование папки
        mock_input.side_effect = ['bank', 'bank2']
        copy_item()
        mock_copytree.assert_called_once_with('bank', 'bank2')

    @patch('os.listdir', return_value=['file1.txt', 'bank', 'file2.txt'])
    def test_list_directory_contents(self, mock_listdir):
        with patch('builtins.print') as mock_print:
            list_directory_contents()
            mock_print.assert_any_call('file1.txt')
            mock_print.assert_any_call('bank')
            mock_print.assert_any_call('file2.txt')

    @patch('os.listdir', return_value=['file1.txt', 'bank', 'file2.txt'])
    def test_list_directories(self, mock_listdir):
        with patch('builtins.print') as mock_print:
            list_directories()
            mock_print.assert_any_call('bank')

    @patch('os.listdir', return_value=['main.py', 'bank', 'quiz.py'])
    def test_list_files(self, mock_listdir):
        with patch('builtins.print') as mock_print:
            list_files()
            mock_print.assert_any_call('main.py')
            mock_print.assert_any_call('quiz.py')

    @patch('os.chdir')
    @patch('builtins.input', side_effect=['/new/directory'])
    def test_change_working_directory(self, mock_input, mock_chdir):
        change_working_directory()
        mock_chdir.assert_called_once_with('/new/directory')
        
    @patch('builtins.input', side_effect=['-50'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_deposit_negative_amount(self, mock_stdout, mock_input):
        deposit()
        self.assertEqual(balance, 0.0)
        self.assertIn('Сумма должна быть положительной.', mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['ten'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_deposit_invalid_input(self, mock_stdout, mock_input):
        deposit()
        self.assertIn('Неверный ввод. Введите числовое значение.', mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['150.0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_make_purchase_insufficient_funds(self, mock_stdout, mock_input):
        global balance
        balance = 100.0
        make_purchase()
        self.assertIn('Недостаточно средств на счете.', mock_stdout.getvalue())
        self.assertEqual(balance, 100.0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_purchase_history_empty(self, mock_stdout):
        show_purchase_history()
        self.assertIn('История покупок пуста.', mock_stdout.getvalue())

    def test_date_to_text(self):
        self.assertEqual(date_to_text('14.03.1879'), 'четырнадцатое марта 1879 года')
        self.assertEqual(date_to_text('07.11.1867'), 'седьмое ноября 1867 года')

    @patch('sys.stdout', new_callable=StringIO)
    def test_os_info_output(self, mock_stdout):
        with patch('platform.processor', return_value='x86_64'):
            with patch('platform.system', return_value='Linux'):
                with patch('platform.release', return_value='5.4.0-42-generic'):
                    with patch('platform.node', return_value='my_machine'):
                        with patch('platform.architecture', return_value=('64bit', '')):
                            os_info()
                            output = mock_stdout.getvalue()
                            expected_output = (
                                "Процессор: x86_64\n"
                                "Система: Linux 5.4.0-42-generic\n"
                                "Имя машины: my_machine\n"
                                "Архитектура: 64bit\n"
                            )
                            self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_program_creator_output(self, mock_stdout):
        program_creator()
        output = mock_stdout.getvalue()
        expected_output = "Создатель программы: via.shcherba\n"
        self.assertEqual(output, expected_output)
        
    def test_save_directory_contents_to_file(self):
        test_files = ['file1.txt', 'file2.txt']
        test_dirs = ['dir1', 'dir2']
        
        for file in test_files:
            with open(file, 'w') as f:
                f.write("This is a test file.")

        for dir in test_dirs:
            os.mkdir(dir)

        save_directory_contents_to_file()
        self.assertTrue(os.path.exists('listdir.txt'))

        with open('listdir.txt', 'r') as f:
            content = f.readlines()

        self.assertEqual(len(content), 2)  
        self.assertTrue(content[0].startswith("files: "))  
        self.assertTrue(content[1].startswith("dirs: "))  

        expected_files = ', '.join(test_files)
        self.assertIn(expected_files, content[0])

        expected_dirs = ', '.join(test_dirs)
        self.assertIn(expected_dirs, content[1])
        
        for file in test_files:
            delete(file)
        for dir in test_dirs:
            delete(dir)

if __name__ == '__main__':
    unittest.main()
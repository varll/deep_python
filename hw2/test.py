import unittest
from unittest.mock import Mock
from faker import Faker
from main import parse_html


class TestHtmlParser(unittest.TestCase):
    def setUp(self):
        self.test_open = Mock()
        self.test_data = Mock()
        self.test_close = Mock()

    def test_empty_text(self):
        test_text = ''
        parse_html(test_text, self.test_open, self.test_data, self.test_close)

        self.assertEqual(self.test_open.call_count, 0)
        self.assertEqual(self.test_close.call_count, 0)
        self.assertEqual(self.test_data.call_count, 0)

        test_text = '       '
        parse_html(test_text, self.test_open, self.test_data, self.test_close)

        self.assertEqual(self.test_open.call_count, 0)
        self.assertEqual(self.test_close.call_count, 0)
        self.assertEqual(self.test_data.call_count, 0)

    def test_empty_data(self):
        test_text = '<html><head><title></title></head></html>'
        tags = []
        parse_html(test_text, tags.append, self.test_data, self.test_close)
        tags_out = ['<html>', '<head>', '<title>']

        self.assertEqual(tags, tags_out)
        self.assertEqual(self.test_data.call_count, 0)
        self.assertEqual(self.test_close.call_count, 3)

    def test_text_with_spaces(self):
        test_text = '  <html><head><title></title></head></html>  '
        tags = []
        parse_html(test_text, tags.append, self.test_data, self.test_close)
        tags_out = ['<html>', '<head>', '<title>']

        self.assertEqual(tags, tags_out)
        self.assertEqual(self.test_data.call_count, 0)
        self.assertEqual(self.test_close.call_count, 3)

    def test_valid_parse(self):
        test_text = ' not<html>testing <head> header   <title>test </title> </head> void</html>   '
        tags = []
        data = []
        parse_html(test_text, tags.append, data.append, self.test_close)

        tags_out = ['<html>', '<head>', '<title>']
        data_out = ['test ', ' header    ', 'testing  void']

        self.assertEqual(tags, tags_out)
        self.assertEqual(data, data_out)
        self.assertEqual(self.test_close.call_count, 3)

    def test_with_factory_boy(self):
        fake = Faker(locale='RU_ru')

        test_text = '<html>' + fake.sentence() + '<h1>' + fake.sentence() + '</h1>' +\
                    '</html>' + '<tag>' + '</tag>'
        parse_html(test_text, self.test_open, self.test_data, self.test_close)

        self.assertEqual(self.test_open.call_count, 3)
        self.assertEqual(self.test_data.call_count, 2)
        self.assertEqual(self.test_close.call_count, 3)


if __name__ == "__main__":
    unittest.main()

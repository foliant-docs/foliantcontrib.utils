import re

from unittest import TestCase
from unittest.mock import Mock

from foliant.preprocessors.utils.preprocessor_ext import BasePreprocessorExt
from foliant.preprocessors.utils.preprocessor_ext import allow_fail


class TestAllowFail(TestCase):
    def test_no_exception(self):
        @allow_fail()
        def test_function(self, arg):
            return arg * 2
        self.assertEqual(test_function(Mock(), 12), 24)

    def test_file_workflow(self):
        @allow_fail()
        def test_function(self, arg):
            raise ValueError('Error')

        preprocessor_mock = Mock()
        result = test_function(preprocessor_mock, 'arg value')

        self.assertIsNone(result)
        preprocessor_mock._warning.assert_called()

    def test_tag_workflow(self):
        @allow_fail()
        def test_function(self, arg):
            raise ValueError('Error')

        preprocessor_mock = Mock()
        result = test_function(preprocessor_mock, re.search('tag', 'source tag source'))

        self.assertEqual(result, 'tag')
        preprocessor_mock._warning.assert_called()
        preprocessor_mock.get_tag_context.assert_called()

    def test_no_args(self):
        @allow_fail()
        def test_function(self):
            raise ValueError('Error')

        preprocessor_mock = Mock()
        result = test_function(preprocessor_mock)

        self.assertIsNone(result)
        preprocessor_mock._warning.assert_called()


class TestGetTagContext(TestCase):
    def test_more_than_limit(self):
        source = 'abcdefghijkl tag long content abcdefghijkl'
        expected = '...defghijkl tag l <...> ntent abcdefghi...'

        m = re.search('tag long content', source)
        self.assertEqual(BasePreprocessorExt.get_tag_context(m, limit=10), expected)

    def test_full_tag(self):
        source = 'abcdefghijkl tag long content abcdefghijkl'
        expected = '...defghijkl tag long content abcdefghi...'

        m = re.search('tag long content', source)
        self.assertEqual(
            BasePreprocessorExt.get_tag_context(m, limit=10, full_tag=True),
            expected
        )

    def test_less_than_limit(self):
        source = 'abcdefghijkl tag long content abcdefghijkl'

        m = re.search('tag long content', source)
        self.assertEqual(BasePreprocessorExt.get_tag_context(m, limit=100), source)

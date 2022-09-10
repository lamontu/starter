
import unittest
from unittest import mock

from class_a import A

class TestA(unittest.TestCase):
    @mock.patch('class_a.postprocess')
    @mock.patch('class_a.sort')  ## can not use 'utils.sort'
    @mock.patch('class_a.preprocess')
    def test_work(self, mock_pre, mock_sort, mock_post):
        mock_pre.return_value = ['pre']
        mock_post.return_value = ['post']
        a = A()
        arr = []
        a.work(arr)
        
        assert mock_pre.called
        assert mock_sort.called
        assert mock_post.called


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

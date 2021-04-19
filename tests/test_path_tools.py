# -*- coding: utf-8 -*-

import os

from unittest import TestCase

from tools.path_tools import check_dir, normalize_path


class TestPathTools(TestCase):
    def test_check_dir_not_exist(self):
        """
        it should raise an exception if the given does not exists
        """
        tmp_dir = os.path.normpath(os.path.join(os.getcwd(), "tmp"))
        with self.assertRaises(Exception):
            check_dir(tmp_dir)

    def test_check_dir_no_files(self):
        """
        it should raise an exception if no file is founded into a given directory
        """
        tmp_dir = os.path.normpath(os.path.join(os.getcwd(), "tmp"))
        os.mkdir(tmp_dir)

        with self.assertRaises(Exception):
            check_dir(tmp_dir)

        os.rmdir(tmp_dir)

    def test_normalize_path(self):
        """
        it should join and normalize a list of path's parts
        """
        parts = [os.getcwd(), "data"]
        expected_path = os.path.normpath(os.path.join(os.getcwd(), "data"))
        result_path = normalize_path(parts)
        self.assertEqual(result_path, expected_path)

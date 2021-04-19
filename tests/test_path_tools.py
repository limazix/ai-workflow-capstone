# -*- coding: utf-8 -*-

import os

from unittest import TestCase

from tools.path_tools import check_dir


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

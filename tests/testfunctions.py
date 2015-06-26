"""Implements the TestFunctions class.
"""


from __future__ import absolute_import
from mock import patch
from unittest import TestCase
from pydvdid.exceptions import DvdPathDoesNotExistException, VideoTsPathDoesNotExistException
from pydvdid.functions import _check_dvd_path_exists, _check_video_ts_path_exists


class TestFunctions(TestCase):
    """Implements a class that contains tests for the pydvdid.functions module.
    """

    @patch("pydvdid.functions.isdir")
    def test__check_dvd_path_exists_does_not_raise_exception_when_path_exists(self, mock_isdir): # pylint: disable=locally-disabled, invalid-name
        """Test that invocation with a valid path does not throw an exception.
        """

        mock_isdir.return_value = True

        try:
            _check_dvd_path_exists("DVD_PATH")
        except Exception as ex: # pylint: disable=locally-disabled, broad-except
            template = "_check_dvd_path_exists raised an exception of type {0} unexpectedly!"
            message = template.format(type(ex).__name__)
            self.fail(message)

        mock_isdir.assert_called_once_with("DVD_PATH")


    @patch("pydvdid.functions.isdir")
    def test__check_dvd_path_exists_does_raise_exception_when_path_does_not_exist(self, mock_isdir): # pylint: disable=locally-disabled, invalid-name
        """Test that invocation with an invalid path throws a DvdPathDoesNotExistException
           exception.
        """

        mock_isdir.return_value = False

        with self.assertRaises(DvdPathDoesNotExistException) as context_manager:
            _check_dvd_path_exists("DVD_PATH")

        mock_isdir.assert_called_once_with("DVD_PATH")

        message = context_manager.exception.message
        self.assertEqual("Path 'DVD_PATH' does not exist.", message)


    @patch("pydvdid.functions.isdir")
    def test__check_video_ts_path_exists_does_not_raise_exception_when_path_exists(self, mock_isdir): # pylint: disable=locally-disabled, invalid-name, line-too-long
        """Test that invocation with a valid path does not throw an exception.
        """

        mock_isdir.return_value = True

        try:
            _check_video_ts_path_exists("DVD_PATH")
        except Exception as ex: # pylint: disable=locally-disabled, broad-except
            template = "_check_video_ts_path_exists raised an exception of type {0} unexpectedly!"
            message = template.format(type(ex).__name__)
            self.fail(message)

        mock_isdir.assert_called_once_with("DVD_PATH/VIDEO_TS")


    @patch("pydvdid.functions.isdir")
    def test__check_video_ts_path_exists_does_raise_exception_when_path_does_not_exist(self, mock_isdir): # pylint: disable=locally-disabled, invalid-name, line-too-long
        """Test that invocation with an invalid path throws a VideoTsPathDoesNotExistException
           exception.
        """

        mock_isdir.return_value = False

        with self.assertRaises(VideoTsPathDoesNotExistException) as context_manager:
            _check_video_ts_path_exists("DVD_PATH")

        mock_isdir.assert_called_once_with("DVD_PATH/VIDEO_TS")

        message = context_manager.exception.message
        self.assertEqual("Path 'DVD_PATH/VIDEO_TS' does not exist.", message)
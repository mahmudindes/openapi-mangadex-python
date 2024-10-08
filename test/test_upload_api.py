# coding: utf-8

"""
    MangaDex API

    MangaDex is an ad-free manga reader offering high-quality images!  This document details our API as it is right now. It is in no way a promise to never change it, although we will endeavour to publicly notify any major change.  # Acceptable use policy  Usage of our services implies acceptance of the following: - You **MUST** credit us - You **MUST** credit scanlation groups if you offer the ability to read chapters - You **CANNOT** run ads or paid services on your website and/or apps  These may change at any time for any and no reason and it is up to you check for updates from time to time.  # Security issues  If you believe you found a security issue in our API, please check our [security.txt](/security.txt) to get in touch privately. 

    The version of the OpenAPI document: 5.10.2
    Contact: support@mangadex.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from mangadex_openapi.api.upload_api import UploadApi


class TestUploadApi(unittest.TestCase):
    """UploadApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UploadApi()

    def tearDown(self) -> None:
        pass

    def test_abandon_upload_session(self) -> None:
        """Test case for abandon_upload_session

        Abandon upload session
        """
        pass

    def test_begin_edit_session(self) -> None:
        """Test case for begin_edit_session

        Start an edit chapter session
        """
        pass

    def test_begin_upload_session(self) -> None:
        """Test case for begin_upload_session

        Start an upload session
        """
        pass

    def test_commit_upload_session(self) -> None:
        """Test case for commit_upload_session

        Commit the upload session and specify chapter data
        """
        pass

    def test_delete_uploaded_session_file(self) -> None:
        """Test case for delete_uploaded_session_file

        Delete an uploaded image from the Upload Session
        """
        pass

    def test_delete_uploaded_session_files(self) -> None:
        """Test case for delete_uploaded_session_files

        Delete a set of uploaded images from the Upload Session
        """
        pass

    def test_get_upload_session(self) -> None:
        """Test case for get_upload_session

        Get the current User upload session
        """
        pass

    def test_put_upload_session_file(self) -> None:
        """Test case for put_upload_session_file

        Upload images to the upload session
        """
        pass

    def test_upload_check_approval_required(self) -> None:
        """Test case for upload_check_approval_required

        Check if a given manga / locale for a User needs moderation approval
        """
        pass


if __name__ == '__main__':
    unittest.main()

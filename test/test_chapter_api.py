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

from mangadex_openapi.api.chapter_api import ChapterApi


class TestChapterApi(unittest.TestCase):
    """ChapterApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ChapterApi()

    def tearDown(self) -> None:
        pass

    def test_delete_chapter_id(self) -> None:
        """Test case for delete_chapter_id

        Delete Chapter
        """
        pass

    def test_get_chapter(self) -> None:
        """Test case for get_chapter

        Chapter list
        """
        pass

    def test_get_chapter_id(self) -> None:
        """Test case for get_chapter_id

        Get Chapter
        """
        pass

    def test_put_chapter_id(self) -> None:
        """Test case for put_chapter_id

        Update Chapter
        """
        pass


if __name__ == '__main__':
    unittest.main()

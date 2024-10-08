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

from mangadex_openapi.models.author_attributes import AuthorAttributes

class TestAuthorAttributes(unittest.TestCase):
    """AuthorAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthorAttributes:
        """Test AuthorAttributes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthorAttributes`
        """
        model = AuthorAttributes()
        if include_optional:
            return AuthorAttributes(
                name = '',
                image_url = '',
                biography = {
                    'key' : 'eiotgsww'
                    },
                twitter = 'https://twitter.com',
                pixiv = 'https://AMDTMv2D2ylmgd10Z3UB6UkJSISSB512iz2DiJy.pixiv.net',
                melon_book = 'https://AMDTMv2D2ylmgd10Z3UB6UkJSISSB512iz2DiJy.melonbooks.co.jp',
                fan_box = 'https://AMDTMv2D2ylmgd10Z3UB6UkJSISSB512iz2DiJy.fanbox.cc',
                booth = 'https://AMDTMv2D2ylmgd10Z3UB6UkJSISSB512iz2DiJy.booth.pm',
                nico_video = 'https://AMDTMv2D2ylmgd10Z3UB6UkJSISSB512iz2DiJy.nicovideo.jp',
                skeb = 'https://AMDTMv2D2ylmgd10Z3UB6UkJSISSB512iz2DiJy.skeb.jp',
                fantia = 'https://AMDTMv2D2ylmgd10Z3UB6UkJSISSB512iz2DiJy.fantia.jp',
                tumblr = 'https://AMDTMv2D2ylmgd10Z3UB6UkJSISSB512iz2DiJy.tumblr.com',
                youtube = 'https://www.youtube.com',
                weibo = 'https://AMDTMv2D2ylmgd10Z3UB6UkJSISSB512iz2DiJy.weibo.com/',
                naver = 'https://AMDTMv2D2ylmgd10Z3UB6UkJSISSB512iz2DiJy.naver.com',
                namicomi = 'https://AMDTMv2D2ylmgd10Z3UB6UkJSISSB512iz2DiJy.namicomi.com',
                website = 'https:/',
                version = 1,
                created_at = '',
                updated_at = ''
            )
        else:
            return AuthorAttributes(
        )
        """

    def testAuthorAttributes(self):
        """Test AuthorAttributes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

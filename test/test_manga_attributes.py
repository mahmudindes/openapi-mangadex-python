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

from mangadex_openapi.models.manga_attributes import MangaAttributes

class TestMangaAttributes(unittest.TestCase):
    """MangaAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MangaAttributes:
        """Test MangaAttributes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MangaAttributes`
        """
        model = MangaAttributes()
        if include_optional:
            return MangaAttributes(
                title = {
                    'key' : 'eiotgsww'
                    },
                alt_titles = [
                    {
                        'key' : 'eiotgsww'
                        }
                    ],
                description = {
                    'key' : 'eiotgsww'
                    },
                is_locked = True,
                links = {
                    'key' : ''
                    },
                original_language = '',
                last_volume = '',
                last_chapter = '',
                publication_demographic = 'shounen',
                status = 'completed',
                year = 56,
                content_rating = 'safe',
                chapter_numbers_reset_on_new_volume = True,
                available_translated_languages = [
                    'ae'
                    ],
                latest_uploaded_chapter = '',
                tags = [
                    mangadex_openapi.models.tag.Tag(
                        id = '', 
                        type = 'tag', 
                        attributes = mangadex_openapi.models.tag_attributes.TagAttributes(
                            name = {
                                'key' : 'eiotgsww'
                                }, 
                            description = {
                                'key' : 'eiotgsww'
                                }, 
                            group = 'content', 
                            version = 1, ), 
                        relationships = [
                            mangadex_openapi.models.relationship.Relationship(
                                id = '', 
                                type = '', 
                                related = 'monochrome', )
                            ], )
                    ],
                state = 'draft',
                version = 1,
                created_at = '',
                updated_at = ''
            )
        else:
            return MangaAttributes(
        )
        """

    def testMangaAttributes(self):
        """Test MangaAttributes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

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

from mangadex_openapi.models.scanlation_group_attributes import ScanlationGroupAttributes

class TestScanlationGroupAttributes(unittest.TestCase):
    """ScanlationGroupAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScanlationGroupAttributes:
        """Test ScanlationGroupAttributes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScanlationGroupAttributes`
        """
        model = ScanlationGroupAttributes()
        if include_optional:
            return ScanlationGroupAttributes(
                name = '',
                alt_names = [
                    {
                        'key' : 'eiotgsww'
                        }
                    ],
                website = '',
                irc_server = '',
                irc_channel = '',
                discord = '',
                contact_email = '',
                description = '',
                twitter = 'https:/',
                manga_updates = 'https://www.mangaupdates.com/publisher/AMDTMv2D2ylmgd10Z3UB6UkJSISSB512iz2DiJy/',
                focused_language = [
                    'ae'
                    ],
                locked = True,
                official = True,
                verified = True,
                inactive = True,
                ex_licensed = True,
                publish_delay = 'P4D',
                version = 1,
                created_at = '',
                updated_at = ''
            )
        else:
            return ScanlationGroupAttributes(
        )
        """

    def testScanlationGroupAttributes(self):
        """Test ScanlationGroupAttributes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

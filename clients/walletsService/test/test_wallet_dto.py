# coding: utf-8

"""
    WalletsService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.1.4089
    Contact: support@fenix-alliance.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.wallet_dto import WalletDto

class TestWalletDto(unittest.TestCase):
    """WalletDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WalletDto:
        """Test WalletDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WalletDto`
        """
        model = WalletDto()
        if include_optional:
            return WalletDto(
                id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                balance = 1.337,
                crypto_balance = 1.337,
                test_mode = True,
                verified = True,
                type = '',
                currency_id = '',
                forex_rate = 1.337,
                balance_in_usd = 1.337,
                main_net_ether_balance = 1.337,
                ethereum_address = '',
                ethereum_public_key = '',
                ethereum_private_key = '',
                rolling_reserve_percent = 1.337
            )
        else:
            return WalletDto(
        )
        """

    def testWalletDto(self):
        """Test WalletDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

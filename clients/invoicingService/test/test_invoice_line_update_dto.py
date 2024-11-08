# coding: utf-8

"""
    InvoicingService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.1.4089
    Contact: support@fenix-alliance.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.invoice_line_update_dto import InvoiceLineUpdateDto

class TestInvoiceLineUpdateDto(unittest.TestCase):
    """InvoiceLineUpdateDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoiceLineUpdateDto:
        """Test InvoiceLineUpdateDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoiceLineUpdateDto`
        """
        model = InvoiceLineUpdateDto()
        if include_optional:
            return InvoiceLineUpdateDto(
                price = 1.337,
                unit_id = '',
                percent = 1.337,
                unit_group_id = '',
                currency_id = '',
                discount_list_id = '',
                rounding_policy_id = '',
                quantity = 56,
                item_id = '',
                item_price_id = '',
                invoice_line_id = '',
                tax_amount_in_usd = 1.337,
                tax_base_amount_in_usd = 1.337
            )
        else:
            return InvoiceLineUpdateDto(
        )
        """

    def testInvoiceLineUpdateDto(self):
        """Test InvoiceLineUpdateDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

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

from openapi_client.models.invoice_reference_create_dto import InvoiceReferenceCreateDto

class TestInvoiceReferenceCreateDto(unittest.TestCase):
    """InvoiceReferenceCreateDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoiceReferenceCreateDto:
        """Test InvoiceReferenceCreateDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoiceReferenceCreateDto`
        """
        model = InvoiceReferenceCreateDto()
        if include_optional:
            return InvoiceReferenceCreateDto(
                id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                tenant_id = '',
                enrollment_id = '',
                referral_invoice_id = '',
                referenced_invoice_id = ''
            )
        else:
            return InvoiceReferenceCreateDto(
        )
        """

    def testInvoiceReferenceCreateDto(self):
        """Test InvoiceReferenceCreateDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
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

from openapi_client.models.invoice_adjustment_dto_envelope import InvoiceAdjustmentDtoEnvelope

class TestInvoiceAdjustmentDtoEnvelope(unittest.TestCase):
    """InvoiceAdjustmentDtoEnvelope unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoiceAdjustmentDtoEnvelope:
        """Test InvoiceAdjustmentDtoEnvelope
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoiceAdjustmentDtoEnvelope`
        """
        model = InvoiceAdjustmentDtoEnvelope()
        if include_optional:
            return InvoiceAdjustmentDtoEnvelope(
                is_success = True,
                error_message = '',
                correlation_id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                activity_id = '',
                result = openapi_client.models.invoice_adjustment_dto.InvoiceAdjustmentDto(
                    id = '', 
                    timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    tenant_id = '', 
                    invoice_id = '', 
                    currency_id = '', 
                    enrollment_id = '', 
                    description = '', 
                    surcharge_percent = 1.337, 
                    surcharge_amount = 1.337, 
                    discount_percent = 1.337, 
                    discount_amount = 1.337, 
                    total_surcharge = 1.337, 
                    total_discount = 1.337, 
                    type = 0, )
            )
        else:
            return InvoiceAdjustmentDtoEnvelope(
        )
        """

    def testInvoiceAdjustmentDtoEnvelope(self):
        """Test InvoiceAdjustmentDtoEnvelope"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

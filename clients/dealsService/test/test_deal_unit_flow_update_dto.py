# coding: utf-8

"""
    DealsService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.1.4089
    Contact: support@fenix-alliance.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.deal_unit_flow_update_dto import DealUnitFlowUpdateDto

class TestDealUnitFlowUpdateDto(unittest.TestCase):
    """DealUnitFlowUpdateDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DealUnitFlowUpdateDto:
        """Test DealUnitFlowUpdateDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DealUnitFlowUpdateDto`
        """
        model = DealUnitFlowUpdateDto()
        if include_optional:
            return DealUnitFlowUpdateDto(
                name = '',
                description = '',
                parent_business_process_id = '01234567891011121314151617181920212223242526272829303132333435',
                tenant_id = '01234567891011121314151617181920212223242526272829303132333435',
                tenant_enrollment_id = '01234567891011121314151617181920212223242526272829303132333435'
            )
        else:
            return DealUnitFlowUpdateDto(
        )
        """

    def testDealUnitFlowUpdateDto(self):
        """Test DealUnitFlowUpdateDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

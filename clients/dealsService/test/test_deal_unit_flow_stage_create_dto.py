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

from openapi_client.models.deal_unit_flow_stage_create_dto import DealUnitFlowStageCreateDto

class TestDealUnitFlowStageCreateDto(unittest.TestCase):
    """DealUnitFlowStageCreateDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DealUnitFlowStageCreateDto:
        """Test DealUnitFlowStageCreateDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DealUnitFlowStageCreateDto`
        """
        model = DealUnitFlowStageCreateDto()
        if include_optional:
            return DealUnitFlowStageCreateDto(
                id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                order = 56,
                name = '',
                deal_unit_flow_id = '',
                tenant_id = '',
                description = '',
                enrolment_id = '',
                parent_business_process_stage_id = ''
            )
        else:
            return DealUnitFlowStageCreateDto(
        )
        """

    def testDealUnitFlowStageCreateDto(self):
        """Test DealUnitFlowStageCreateDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

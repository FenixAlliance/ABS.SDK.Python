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

from openapi_client.models.deal_unit_flow_stage_update_dto import DealUnitFlowStageUpdateDto

class TestDealUnitFlowStageUpdateDto(unittest.TestCase):
    """DealUnitFlowStageUpdateDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DealUnitFlowStageUpdateDto:
        """Test DealUnitFlowStageUpdateDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DealUnitFlowStageUpdateDto`
        """
        model = DealUnitFlowStageUpdateDto()
        if include_optional:
            return DealUnitFlowStageUpdateDto(
                order = 56,
                name = '',
                description = '',
                enrolment_id = '',
                deal_unit_flow_id = '',
                parent_business_process_stage_id = ''
            )
        else:
            return DealUnitFlowStageUpdateDto(
        )
        """

    def testDealUnitFlowStageUpdateDto(self):
        """Test DealUnitFlowStageUpdateDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

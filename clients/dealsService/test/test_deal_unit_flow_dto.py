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

from openapi_client.models.deal_unit_flow_dto import DealUnitFlowDto

class TestDealUnitFlowDto(unittest.TestCase):
    """DealUnitFlowDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DealUnitFlowDto:
        """Test DealUnitFlowDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DealUnitFlowDto`
        """
        model = DealUnitFlowDto()
        if include_optional:
            return DealUnitFlowDto(
                id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                description = '',
                parent_business_process_id = '',
                tenant_id = '',
                tenant_enrolment_id = ''
            )
        else:
            return DealUnitFlowDto(
        )
        """

    def testDealUnitFlowDto(self):
        """Test DealUnitFlowDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

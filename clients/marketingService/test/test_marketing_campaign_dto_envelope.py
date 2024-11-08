# coding: utf-8

"""
    MarketingService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.1.4089
    Contact: support@fenix-alliance.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.marketing_campaign_dto_envelope import MarketingCampaignDtoEnvelope

class TestMarketingCampaignDtoEnvelope(unittest.TestCase):
    """MarketingCampaignDtoEnvelope unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MarketingCampaignDtoEnvelope:
        """Test MarketingCampaignDtoEnvelope
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MarketingCampaignDtoEnvelope`
        """
        model = MarketingCampaignDtoEnvelope()
        if include_optional:
            return MarketingCampaignDtoEnvelope(
                is_success = True,
                error_message = '',
                correlation_id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                activity_id = '',
                result = openapi_client.models.marketing_campaign_dto.MarketingCampaignDto(
                    id = '', 
                    timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    name = '', 
                    offer = '', 
                    active = True, 
                    proposed_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    proposed_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    actual_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    actual_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    code = '', 
                    allocated_budget = 1.337, 
                    activity_cost = 1.337, 
                    misc_cost = 1.337, 
                    expected_response_percent = 1.337, 
                    marketing_area_id = '', 
                    currency_id = '', 
                    tenant_id = '', 
                    enrolment_id = '', )
            )
        else:
            return MarketingCampaignDtoEnvelope(
        )
        """

    def testMarketingCampaignDtoEnvelope(self):
        """Test MarketingCampaignDtoEnvelope"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

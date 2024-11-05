# coding: utf-8

"""
    SupportService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.1.4089
    Contact: support@fenix-alliance.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.support_ticket_dto import SupportTicketDto

class TestSupportTicketDto(unittest.TestCase):
    """SupportTicketDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SupportTicketDto:
        """Test SupportTicketDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SupportTicketDto`
        """
        model = SupportTicketDto()
        if include_optional:
            return SupportTicketDto(
                id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                description = '',
                account_holder_id = '',
                contact_id = '',
                business_id = '',
                business_profile_record_id = '',
                support_ticket_type_id = '',
                support_entitlement_id = '',
                support_priority_id = ''
            )
        else:
            return SupportTicketDto(
        )
        """

    def testSupportTicketDto(self):
        """Test SupportTicketDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
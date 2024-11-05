# coding: utf-8

"""
    TimeTrackerService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.1.4089
    Contact: support@fenix-alliance.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.project_time_log_dto_list_envelope import ProjectTimeLogDtoListEnvelope

class TestProjectTimeLogDtoListEnvelope(unittest.TestCase):
    """ProjectTimeLogDtoListEnvelope unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectTimeLogDtoListEnvelope:
        """Test ProjectTimeLogDtoListEnvelope
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectTimeLogDtoListEnvelope`
        """
        model = ProjectTimeLogDtoListEnvelope()
        if include_optional:
            return ProjectTimeLogDtoListEnvelope(
                is_success = True,
                error_message = '',
                correlation_id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                activity_id = '',
                result = [
                    openapi_client.models.project_time_log_dto.ProjectTimeLogDto(
                        id = '', 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        project_id = '', 
                        project_task_id = '', 
                        task_category_id = '', 
                        project_period_id = '', 
                        responsible_contact_id = '', 
                        creator_contact_id = '', 
                        record_type = 0, 
                        time_stamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_span = 'PT2H30M', 
                        log_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        comments = '', 
                        type = '', )
                    ]
            )
        else:
            return ProjectTimeLogDtoListEnvelope(
        )
        """

    def testProjectTimeLogDtoListEnvelope(self):
        """Test ProjectTimeLogDtoListEnvelope"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

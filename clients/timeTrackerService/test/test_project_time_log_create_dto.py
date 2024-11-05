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

from openapi_client.models.project_time_log_create_dto import ProjectTimeLogCreateDto

class TestProjectTimeLogCreateDto(unittest.TestCase):
    """ProjectTimeLogCreateDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectTimeLogCreateDto:
        """Test ProjectTimeLogCreateDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectTimeLogCreateDto`
        """
        model = ProjectTimeLogCreateDto()
        if include_optional:
            return ProjectTimeLogCreateDto(
                id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                time_span = 'PT2H30M',
                log_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                comments = '',
                project_task_id = '0',
                project_period_id = '0',
                project_time_log_record_type = 0,
                project_id = ''
            )
        else:
            return ProjectTimeLogCreateDto(
                project_task_id = '0',
                project_period_id = '0',
        )
        """

    def testProjectTimeLogCreateDto(self):
        """Test ProjectTimeLogCreateDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

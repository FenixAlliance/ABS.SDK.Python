# coding: utf-8

"""
    ProjectsService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.1.4089
    Contact: support@fenix-alliance.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.task_type_dto import TaskTypeDto

class TestTaskTypeDto(unittest.TestCase):
    """TaskTypeDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TaskTypeDto:
        """Test TaskTypeDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TaskTypeDto`
        """
        model = TaskTypeDto()
        if include_optional:
            return TaskTypeDto(
                id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                title = '',
                task_category_id = '',
                display_in_time_tracker = True,
                requires_description = True
            )
        else:
            return TaskTypeDto(
        )
        """

    def testTaskTypeDto(self):
        """Test TaskTypeDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
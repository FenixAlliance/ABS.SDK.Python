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

from openapi_client.models.task_category_update_dto import TaskCategoryUpdateDto

class TestTaskCategoryUpdateDto(unittest.TestCase):
    """TaskCategoryUpdateDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TaskCategoryUpdateDto:
        """Test TaskCategoryUpdateDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TaskCategoryUpdateDto`
        """
        model = TaskCategoryUpdateDto()
        if include_optional:
            return TaskCategoryUpdateDto(
                title = ''
            )
        else:
            return TaskCategoryUpdateDto(
        )
        """

    def testTaskCategoryUpdateDto(self):
        """Test TaskCategoryUpdateDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

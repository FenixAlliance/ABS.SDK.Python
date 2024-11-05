# coding: utf-8

# flake8: noqa

"""
    TimeTrackerService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.1.4089
    Contact: support@fenix-alliance.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from openapi_client.api.project_time_logs_api import ProjectTimeLogsApi
from openapi_client.api.time_log_approvals_api import TimeLogApprovalsApi

# import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.exceptions import OpenApiException
from openapi_client.exceptions import ApiTypeError
from openapi_client.exceptions import ApiValueError
from openapi_client.exceptions import ApiKeyError
from openapi_client.exceptions import ApiAttributeError
from openapi_client.exceptions import ApiException

# import models into sdk package
from openapi_client.models.error_envelope import ErrorEnvelope
from openapi_client.models.project_hours_approval_approver_update_dto import ProjectHoursApprovalApproverUpdateDto
from openapi_client.models.project_hours_approval_create_dto import ProjectHoursApprovalCreateDto
from openapi_client.models.project_hours_approval_status_update_dto import ProjectHoursApprovalStatusUpdateDto
from openapi_client.models.project_time_log_create_dto import ProjectTimeLogCreateDto
from openapi_client.models.project_time_log_dto import ProjectTimeLogDto
from openapi_client.models.project_time_log_dto_envelope import ProjectTimeLogDtoEnvelope
from openapi_client.models.project_time_log_dto_list_envelope import ProjectTimeLogDtoListEnvelope
from openapi_client.models.project_time_log_update_dto import ProjectTimeLogUpdateDto
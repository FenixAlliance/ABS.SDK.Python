# coding: utf-8

# flake8: noqa

"""
    HrmsService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.1.4089
    Contact: support@fenix-alliance.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from openapi_client.api.employees_api import EmployeesApi
from openapi_client.api.employers_api import EmployersApi
from openapi_client.api.gigs_api import GigsApi
from openapi_client.api.job_offers_api import JobOffersApi

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
from openapi_client.models.employee_profile_create_dto import EmployeeProfileCreateDto
from openapi_client.models.employee_profile_dto import EmployeeProfileDto
from openapi_client.models.employee_profile_dto_envelope import EmployeeProfileDtoEnvelope
from openapi_client.models.employee_profile_dto_list_envelope import EmployeeProfileDtoListEnvelope
from openapi_client.models.employer_profile_create_dto import EmployerProfileCreateDto
from openapi_client.models.employer_profile_dto import EmployerProfileDto
from openapi_client.models.employer_profile_dto_envelope import EmployerProfileDtoEnvelope
from openapi_client.models.employer_profile_dto_list_envelope import EmployerProfileDtoListEnvelope
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.error_envelope import ErrorEnvelope
from openapi_client.models.gig_create_dto import GigCreateDto
from openapi_client.models.gig_dto import GigDto
from openapi_client.models.gig_dto_envelope import GigDtoEnvelope
from openapi_client.models.gig_dto_list_envelope import GigDtoListEnvelope
from openapi_client.models.int32_envelope import Int32Envelope
from openapi_client.models.job_offer_create_dto import JobOfferCreateDto
from openapi_client.models.job_offer_dto import JobOfferDto
from openapi_client.models.job_offer_dto_envelope import JobOfferDtoEnvelope
from openapi_client.models.job_offer_dto_list_envelope import JobOfferDtoListEnvelope
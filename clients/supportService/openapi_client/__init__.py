# coding: utf-8

# flake8: noqa

"""
    SupportService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.1.4089
    Contact: support@fenix-alliance.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from openapi_client.api.support_entitlements_api import SupportEntitlementsApi
from openapi_client.api.support_request_attachments_api import SupportRequestAttachmentsApi
from openapi_client.api.support_requests_api import SupportRequestsApi
from openapi_client.api.support_ticket_priorities_api import SupportTicketPrioritiesApi
from openapi_client.api.support_ticket_types_api import SupportTicketTypesApi
from openapi_client.api.support_tickets_api import SupportTicketsApi

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
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.error_envelope import ErrorEnvelope
from openapi_client.models.int32_envelope import Int32Envelope
from openapi_client.models.private_message_dto import PrivateMessageDto
from openapi_client.models.private_message_dto_list_envelope import PrivateMessageDtoListEnvelope
from openapi_client.models.support_entitlement_create_dto import SupportEntitlementCreateDto
from openapi_client.models.support_entitlement_dto import SupportEntitlementDto
from openapi_client.models.support_entitlement_dto_envelope import SupportEntitlementDtoEnvelope
from openapi_client.models.support_entitlement_dto_list_envelope import SupportEntitlementDtoListEnvelope
from openapi_client.models.support_entitlement_update_dto import SupportEntitlementUpdateDto
from openapi_client.models.support_request_attachment_create_dto import SupportRequestAttachmentCreateDto
from openapi_client.models.support_request_attachment_dto import SupportRequestAttachmentDto
from openapi_client.models.support_request_attachment_dto_envelope import SupportRequestAttachmentDtoEnvelope
from openapi_client.models.support_request_attachment_dto_list_envelope import SupportRequestAttachmentDtoListEnvelope
from openapi_client.models.support_request_attachment_update_dto import SupportRequestAttachmentUpdateDto
from openapi_client.models.support_request_create_dto import SupportRequestCreateDto
from openapi_client.models.support_request_dto import SupportRequestDto
from openapi_client.models.support_request_dto_envelope import SupportRequestDtoEnvelope
from openapi_client.models.support_request_dto_list_envelope import SupportRequestDtoListEnvelope
from openapi_client.models.support_request_update_dto import SupportRequestUpdateDto
from openapi_client.models.support_ticket_conversation_create_dto import SupportTicketConversationCreateDto
from openapi_client.models.support_ticket_conversation_dto import SupportTicketConversationDto
from openapi_client.models.support_ticket_conversation_dto_envelope import SupportTicketConversationDtoEnvelope
from openapi_client.models.support_ticket_conversation_dto_list_envelope import SupportTicketConversationDtoListEnvelope
from openapi_client.models.support_ticket_create_dto import SupportTicketCreateDto
from openapi_client.models.support_ticket_dto import SupportTicketDto
from openapi_client.models.support_ticket_dto_envelope import SupportTicketDtoEnvelope
from openapi_client.models.support_ticket_dto_list_envelope import SupportTicketDtoListEnvelope
from openapi_client.models.support_ticket_priority_create_dto import SupportTicketPriorityCreateDto
from openapi_client.models.support_ticket_priority_dto import SupportTicketPriorityDto
from openapi_client.models.support_ticket_priority_dto_envelope import SupportTicketPriorityDtoEnvelope
from openapi_client.models.support_ticket_priority_dto_list_envelope import SupportTicketPriorityDtoListEnvelope
from openapi_client.models.support_ticket_priority_update_dto import SupportTicketPriorityUpdateDto
from openapi_client.models.support_ticket_type_create_dto import SupportTicketTypeCreateDto
from openapi_client.models.support_ticket_type_dto import SupportTicketTypeDto
from openapi_client.models.support_ticket_type_dto_envelope import SupportTicketTypeDtoEnvelope
from openapi_client.models.support_ticket_type_dto_list_envelope import SupportTicketTypeDtoListEnvelope
from openapi_client.models.support_ticket_type_update_dto import SupportTicketTypeUpdateDto
from openapi_client.models.support_ticket_update_dto import SupportTicketUpdateDto
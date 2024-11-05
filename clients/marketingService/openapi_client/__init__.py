# coding: utf-8

# flake8: noqa

"""
    MarketingService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.1.4089
    Contact: support@fenix-alliance.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from openapi_client.api.email_groups_api import EmailGroupsApi
from openapi_client.api.email_signatures_api import EmailSignaturesApi
from openapi_client.api.email_templates_api import EmailTemplatesApi
from openapi_client.api.marketing_campaigns_api import MarketingCampaignsApi
from openapi_client.api.marketing_lists_api import MarketingListsApi
from openapi_client.api.newsletters_api import NewslettersApi
from openapi_client.api.social_media_posts_api import SocialMediaPostsApi
from openapi_client.api.social_post_buckets_api import SocialPostBucketsApi
from openapi_client.api.tracking_pixels_api import TrackingPixelsApi

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
from openapi_client.models.currency import Currency
from openapi_client.models.email_group_create_dto import EmailGroupCreateDto
from openapi_client.models.email_group_dto import EmailGroupDto
from openapi_client.models.email_group_dto_envelope import EmailGroupDtoEnvelope
from openapi_client.models.email_group_dto_list_envelope import EmailGroupDtoListEnvelope
from openapi_client.models.email_group_update_dto import EmailGroupUpdateDto
from openapi_client.models.email_signature_create_dto import EmailSignatureCreateDto
from openapi_client.models.email_signature_dto import EmailSignatureDto
from openapi_client.models.email_signature_dto_envelope import EmailSignatureDtoEnvelope
from openapi_client.models.email_signature_dto_list_envelope import EmailSignatureDtoListEnvelope
from openapi_client.models.email_signature_update_dto import EmailSignatureUpdateDto
from openapi_client.models.email_template_create_dto import EmailTemplateCreateDto
from openapi_client.models.email_template_dto import EmailTemplateDto
from openapi_client.models.email_template_dto_envelope import EmailTemplateDtoEnvelope
from openapi_client.models.email_template_dto_list_envelope import EmailTemplateDtoListEnvelope
from openapi_client.models.email_template_update_dto import EmailTemplateUpdateDto
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.error_envelope import ErrorEnvelope
from openapi_client.models.int32_envelope import Int32Envelope
from openapi_client.models.marketing_campaign_create_dto import MarketingCampaignCreateDto
from openapi_client.models.marketing_campaign_dto import MarketingCampaignDto
from openapi_client.models.marketing_campaign_dto_envelope import MarketingCampaignDtoEnvelope
from openapi_client.models.marketing_campaign_update_dto import MarketingCampaignUpdateDto
from openapi_client.models.marketing_list_create_dto import MarketingListCreateDto
from openapi_client.models.marketing_list_dto import MarketingListDto
from openapi_client.models.marketing_list_dto_envelope import MarketingListDtoEnvelope
from openapi_client.models.marketing_list_dto_list_envelope import MarketingListDtoListEnvelope
from openapi_client.models.marketing_list_update_dto import MarketingListUpdateDto
from openapi_client.models.money import Money
from openapi_client.models.newsletter_create_dto import NewsletterCreateDto
from openapi_client.models.newsletter_dto import NewsletterDto
from openapi_client.models.newsletter_dto_envelope import NewsletterDtoEnvelope
from openapi_client.models.newsletter_update_dto import NewsletterUpdateDto
from openapi_client.models.order_dto import OrderDto
from openapi_client.models.order_dto_envelope import OrderDtoEnvelope
from openapi_client.models.social_media_post_create_dto import SocialMediaPostCreateDto
from openapi_client.models.social_media_post_dto import SocialMediaPostDto
from openapi_client.models.social_media_post_dto_envelope import SocialMediaPostDtoEnvelope
from openapi_client.models.social_media_post_dto_list_envelope import SocialMediaPostDtoListEnvelope
from openapi_client.models.social_media_post_update_dto import SocialMediaPostUpdateDto
from openapi_client.models.social_post_bucket_create_dto import SocialPostBucketCreateDto
from openapi_client.models.social_post_bucket_dto import SocialPostBucketDto
from openapi_client.models.social_post_bucket_dto_envelope import SocialPostBucketDtoEnvelope
from openapi_client.models.social_post_bucket_dto_list_envelope import SocialPostBucketDtoListEnvelope
from openapi_client.models.social_post_bucket_update_dto import SocialPostBucketUpdateDto

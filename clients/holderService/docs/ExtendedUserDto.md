# ExtendedUserDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**full_name** | **str** |  | [optional] [readonly] 
**qualified_name** | **str** |  | [optional] 
**public_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**cover_url** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**git_hub_url** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**timezone_id** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**twitter_url** | **str** |  | [optional] 
**you_tube_url** | **str** |  | [optional] 
**linked_in_url** | **str** |  | [optional] 
**facebook_url** | **str** |  | [optional] 
**instagram_url** | **str** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 
**birthday** | **datetime** |  | [optional] 
**id_provider** | **str** |  | [optional] 
**language_id** | **str** |  | [optional] 
**gender** | **int** |  | [optional] 
**city_id** | **str** |  | [optional] 
**state_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**about** | **str** |  | [optional] 
**job_title** | **str** |  | [optional] 
**social_feed_id** | **str** |  | [optional] 
**current_tenant_id** | **str** |  | [optional] 
**current_enrollment_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**cart_id** | **str** |  | [optional] 
**wallet_id** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**public_identifier** | **str** |  | [optional] 
**identity_provider** | **str** |  | [optional] 
**phone_number_confirmed** | **bool** |  | [optional] 
**email_confirmed** | **bool** |  | [optional] 
**availability** | **int** |  | [optional] 
**lockout_enabled** | **bool** |  | [optional] 
**lockout_end** | **datetime** |  | [optional] 
**enrollments_count** | **int** |  | [optional] 
**site_theme** | **int** |  | [optional] 
**cart** | [**CartDto**](CartDto.md) |  | [optional] 
**wallet** | [**WalletDto**](WalletDto.md) |  | [optional] 
**social_profile** | [**SocialProfileDto**](SocialProfileDto.md) |  | [optional] 
**settings** | [**UserSettingsDto**](UserSettingsDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.extended_user_dto import ExtendedUserDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedUserDto from a JSON string
extended_user_dto_instance = ExtendedUserDto.from_json(json)
# print the JSON string representation of the object
print(ExtendedUserDto.to_json())

# convert the object into a dict
extended_user_dto_dict = extended_user_dto_instance.to_dict()
# create an instance of ExtendedUserDto from a dict
extended_user_dto_from_dict = ExtendedUserDto.from_dict(extended_user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



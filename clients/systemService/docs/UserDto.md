# UserDto


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

## Example

```python
from openapi_client.models.user_dto import UserDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserDto from a JSON string
user_dto_instance = UserDto.from_json(json)
# print the JSON string representation of the object
print(UserDto.to_json())

# convert the object into a dict
user_dto_dict = user_dto_instance.to_dict()
# create an instance of UserDto from a dict
user_dto_from_dict = UserDto.from_dict(user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



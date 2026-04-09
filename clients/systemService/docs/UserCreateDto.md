# UserCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**qualified_name** | **str** |  | [optional] 
**birthday** | **datetime** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**public_name** | **str** |  | [optional] 
**id_provider** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**about** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**job_title** | **str** |  | [optional] 
**git_hub_url** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**twitter_url** | **str** |  | [optional] 
**facebook_url** | **str** |  | [optional] 
**you_tube_url** | **str** |  | [optional] 
**linked_in_url** | **str** |  | [optional] 
**instagram_url** | **str** |  | [optional] 
**timezone_id** | **str** |  | [optional] 
**language_id** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**state_id** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.user_create_dto import UserCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreateDto from a JSON string
user_create_dto_instance = UserCreateDto.from_json(json)
# print the JSON string representation of the object
print(UserCreateDto.to_json())

# convert the object into a dict
user_create_dto_dict = user_create_dto_instance.to_dict()
# create an instance of UserCreateDto from a dict
user_create_dto_from_dict = UserCreateDto.from_dict(user_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



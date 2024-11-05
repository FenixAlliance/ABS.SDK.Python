# SimpleUserDto


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

## Example

```python
from openapi_client.models.simple_user_dto import SimpleUserDto

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleUserDto from a JSON string
simple_user_dto_instance = SimpleUserDto.from_json(json)
# print the JSON string representation of the object
print(SimpleUserDto.to_json())

# convert the object into a dict
simple_user_dto_dict = simple_user_dto_instance.to_dict()
# create an instance of SimpleUserDto from a dict
simple_user_dto_from_dict = SimpleUserDto.from_dict(simple_user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



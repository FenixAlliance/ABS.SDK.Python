# SocialGroupDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**business_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.social_group_dto import SocialGroupDto

# TODO update the JSON string below
json = "{}"
# create an instance of SocialGroupDto from a JSON string
social_group_dto_instance = SocialGroupDto.from_json(json)
# print the JSON string representation of the object
print(SocialGroupDto.to_json())

# convert the object into a dict
social_group_dto_dict = social_group_dto_instance.to_dict()
# create an instance of SocialGroupDto from a dict
social_group_dto_from_dict = SocialGroupDto.from_dict(social_group_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



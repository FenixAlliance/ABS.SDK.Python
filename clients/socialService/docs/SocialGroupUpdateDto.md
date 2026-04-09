# SocialGroupUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.social_group_update_dto import SocialGroupUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SocialGroupUpdateDto from a JSON string
social_group_update_dto_instance = SocialGroupUpdateDto.from_json(json)
# print the JSON string representation of the object
print(SocialGroupUpdateDto.to_json())

# convert the object into a dict
social_group_update_dto_dict = social_group_update_dto_instance.to_dict()
# create an instance of SocialGroupUpdateDto from a dict
social_group_update_dto_from_dict = SocialGroupUpdateDto.from_dict(social_group_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



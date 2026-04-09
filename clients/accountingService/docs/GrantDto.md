# GrantDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.grant_dto import GrantDto

# TODO update the JSON string below
json = "{}"
# create an instance of GrantDto from a JSON string
grant_dto_instance = GrantDto.from_json(json)
# print the JSON string representation of the object
print(GrantDto.to_json())

# convert the object into a dict
grant_dto_dict = grant_dto_instance.to_dict()
# create an instance of GrantDto from a dict
grant_dto_from_dict = GrantDto.from_dict(grant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



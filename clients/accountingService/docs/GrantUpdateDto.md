# GrantUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.grant_update_dto import GrantUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of GrantUpdateDto from a JSON string
grant_update_dto_instance = GrantUpdateDto.from_json(json)
# print the JSON string representation of the object
print(GrantUpdateDto.to_json())

# convert the object into a dict
grant_update_dto_dict = grant_update_dto_instance.to_dict()
# create an instance of GrantUpdateDto from a dict
grant_update_dto_from_dict = GrantUpdateDto.from_dict(grant_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AccountGroupCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**parent_account_group_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.account_group_create_dto import AccountGroupCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccountGroupCreateDto from a JSON string
account_group_create_dto_instance = AccountGroupCreateDto.from_json(json)
# print the JSON string representation of the object
print(AccountGroupCreateDto.to_json())

# convert the object into a dict
account_group_create_dto_dict = account_group_create_dto_instance.to_dict()
# create an instance of AccountGroupCreateDto from a dict
account_group_create_dto_from_dict = AccountGroupCreateDto.from_dict(account_group_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



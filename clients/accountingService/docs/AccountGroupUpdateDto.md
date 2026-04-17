# AccountGroupUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**parent_account_group_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.account_group_update_dto import AccountGroupUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccountGroupUpdateDto from a JSON string
account_group_update_dto_instance = AccountGroupUpdateDto.from_json(json)
# print the JSON string representation of the object
print(AccountGroupUpdateDto.to_json())

# convert the object into a dict
account_group_update_dto_dict = account_group_update_dto_instance.to_dict()
# create an instance of AccountGroupUpdateDto from a dict
account_group_update_dto_from_dict = AccountGroupUpdateDto.from_dict(account_group_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



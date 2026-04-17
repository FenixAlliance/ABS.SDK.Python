# AccountTypeUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.account_type_update_dto import AccountTypeUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTypeUpdateDto from a JSON string
account_type_update_dto_instance = AccountTypeUpdateDto.from_json(json)
# print the JSON string representation of the object
print(AccountTypeUpdateDto.to_json())

# convert the object into a dict
account_type_update_dto_dict = account_type_update_dto_instance.to_dict()
# create an instance of AccountTypeUpdateDto from a dict
account_type_update_dto_from_dict = AccountTypeUpdateDto.from_dict(account_type_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AccountTypeCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.account_type_create_dto import AccountTypeCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTypeCreateDto from a JSON string
account_type_create_dto_instance = AccountTypeCreateDto.from_json(json)
# print the JSON string representation of the object
print(AccountTypeCreateDto.to_json())

# convert the object into a dict
account_type_create_dto_dict = account_type_create_dto_instance.to_dict()
# create an instance of AccountTypeCreateDto from a dict
account_type_create_dto_from_dict = AccountTypeCreateDto.from_dict(account_type_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



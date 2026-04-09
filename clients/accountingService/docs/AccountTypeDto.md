# AccountTypeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.account_type_dto import AccountTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTypeDto from a JSON string
account_type_dto_instance = AccountTypeDto.from_json(json)
# print the JSON string representation of the object
print(AccountTypeDto.to_json())

# convert the object into a dict
account_type_dto_dict = account_type_dto_instance.to_dict()
# create an instance of AccountTypeDto from a dict
account_type_dto_from_dict = AccountTypeDto.from_dict(account_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



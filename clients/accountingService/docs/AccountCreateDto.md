# AccountCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**group** | **bool** |  | [optional] 
**frozen** | **bool** |  | [optional] 
**name** | **str** |  | 
**code** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**currency_id** | **str** |  | 
**enrollment_id** | **str** |  | [optional] 
**account_type_id** | **str** |  | [optional] 
**parent_account_id** | **str** |  | [optional] 
**account_category** | **str** |  | 

## Example

```python
from openapi_client.models.account_create_dto import AccountCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccountCreateDto from a JSON string
account_create_dto_instance = AccountCreateDto.from_json(json)
# print the JSON string representation of the object
print(AccountCreateDto.to_json())

# convert the object into a dict
account_create_dto_dict = account_create_dto_instance.to_dict()
# create an instance of AccountCreateDto from a dict
account_create_dto_from_dict = AccountCreateDto.from_dict(account_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



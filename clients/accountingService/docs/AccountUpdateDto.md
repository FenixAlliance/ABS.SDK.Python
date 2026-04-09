# AccountUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **bool** |  | [optional] 
**frozen** | **bool** |  | [optional] 
**name** | **str** |  | 
**code** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**currency_id** | **str** |  | 
**account_type_id** | **str** |  | [optional] 
**parent_account_id** | **str** |  | [optional] 
**account_category** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.account_update_dto import AccountUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccountUpdateDto from a JSON string
account_update_dto_instance = AccountUpdateDto.from_json(json)
# print the JSON string representation of the object
print(AccountUpdateDto.to_json())

# convert the object into a dict
account_update_dto_dict = account_update_dto_instance.to_dict()
# create an instance of AccountUpdateDto from a dict
account_update_dto_from_dict = AccountUpdateDto.from_dict(account_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



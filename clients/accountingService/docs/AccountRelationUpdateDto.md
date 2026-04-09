# AccountRelationUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.account_relation_update_dto import AccountRelationUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccountRelationUpdateDto from a JSON string
account_relation_update_dto_instance = AccountRelationUpdateDto.from_json(json)
# print the JSON string representation of the object
print(AccountRelationUpdateDto.to_json())

# convert the object into a dict
account_relation_update_dto_dict = account_relation_update_dto_instance.to_dict()
# create an instance of AccountRelationUpdateDto from a dict
account_relation_update_dto_from_dict = AccountRelationUpdateDto.from_dict(account_relation_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



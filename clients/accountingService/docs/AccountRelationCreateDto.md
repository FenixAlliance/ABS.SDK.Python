# AccountRelationCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**account_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.account_relation_create_dto import AccountRelationCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccountRelationCreateDto from a JSON string
account_relation_create_dto_instance = AccountRelationCreateDto.from_json(json)
# print the JSON string representation of the object
print(AccountRelationCreateDto.to_json())

# convert the object into a dict
account_relation_create_dto_dict = account_relation_create_dto_instance.to_dict()
# create an instance of AccountRelationCreateDto from a dict
account_relation_create_dto_from_dict = AccountRelationCreateDto.from_dict(account_relation_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



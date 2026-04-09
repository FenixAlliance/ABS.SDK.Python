# AccountRelationDto


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
from openapi_client.models.account_relation_dto import AccountRelationDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccountRelationDto from a JSON string
account_relation_dto_instance = AccountRelationDto.from_json(json)
# print the JSON string representation of the object
print(AccountRelationDto.to_json())

# convert the object into a dict
account_relation_dto_dict = account_relation_dto_instance.to_dict()
# create an instance of AccountRelationDto from a dict
account_relation_dto_from_dict = AccountRelationDto.from_dict(account_relation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



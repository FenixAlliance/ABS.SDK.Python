# CreateLedgerDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**date_time** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**ledger_type_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.create_ledger_dto import CreateLedgerDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLedgerDto from a JSON string
create_ledger_dto_instance = CreateLedgerDto.from_json(json)
# print the JSON string representation of the object
print(CreateLedgerDto.to_json())

# convert the object into a dict
create_ledger_dto_dict = create_ledger_dto_instance.to_dict()
# create an instance of CreateLedgerDto from a dict
create_ledger_dto_from_dict = CreateLedgerDto.from_dict(create_ledger_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



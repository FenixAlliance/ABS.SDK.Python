# UpdateLedgerDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**ledger_type_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.update_ledger_dto import UpdateLedgerDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateLedgerDto from a JSON string
update_ledger_dto_instance = UpdateLedgerDto.from_json(json)
# print the JSON string representation of the object
print(UpdateLedgerDto.to_json())

# convert the object into a dict
update_ledger_dto_dict = update_ledger_dto_instance.to_dict()
# create an instance of UpdateLedgerDto from a dict
update_ledger_dto_from_dict = UpdateLedgerDto.from_dict(update_ledger_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



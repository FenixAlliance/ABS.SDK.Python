# LedgerDto


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
from openapi_client.models.ledger_dto import LedgerDto

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerDto from a JSON string
ledger_dto_instance = LedgerDto.from_json(json)
# print the JSON string representation of the object
print(LedgerDto.to_json())

# convert the object into a dict
ledger_dto_dict = ledger_dto_instance.to_dict()
# create an instance of LedgerDto from a dict
ledger_dto_from_dict = LedgerDto.from_dict(ledger_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



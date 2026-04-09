# LedgerTypeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**ledger_class** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ledger_type_dto import LedgerTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerTypeDto from a JSON string
ledger_type_dto_instance = LedgerTypeDto.from_json(json)
# print the JSON string representation of the object
print(LedgerTypeDto.to_json())

# convert the object into a dict
ledger_type_dto_dict = ledger_type_dto_instance.to_dict()
# create an instance of LedgerTypeDto from a dict
ledger_type_dto_from_dict = LedgerTypeDto.from_dict(ledger_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



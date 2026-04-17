# LedgerTypeCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**ledger_class** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ledger_type_create_dto import LedgerTypeCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerTypeCreateDto from a JSON string
ledger_type_create_dto_instance = LedgerTypeCreateDto.from_json(json)
# print the JSON string representation of the object
print(LedgerTypeCreateDto.to_json())

# convert the object into a dict
ledger_type_create_dto_dict = ledger_type_create_dto_instance.to_dict()
# create an instance of LedgerTypeCreateDto from a dict
ledger_type_create_dto_from_dict = LedgerTypeCreateDto.from_dict(ledger_type_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



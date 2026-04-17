# LedgerTypeUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**ledger_class** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ledger_type_update_dto import LedgerTypeUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerTypeUpdateDto from a JSON string
ledger_type_update_dto_instance = LedgerTypeUpdateDto.from_json(json)
# print the JSON string representation of the object
print(LedgerTypeUpdateDto.to_json())

# convert the object into a dict
ledger_type_update_dto_dict = ledger_type_update_dto_instance.to_dict()
# create an instance of LedgerTypeUpdateDto from a dict
ledger_type_update_dto_from_dict = LedgerTypeUpdateDto.from_dict(ledger_type_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



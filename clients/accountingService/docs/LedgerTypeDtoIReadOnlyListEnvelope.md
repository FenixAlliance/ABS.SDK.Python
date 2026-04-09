# LedgerTypeDtoIReadOnlyListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[LedgerTypeDto]**](LedgerTypeDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.ledger_type_dto_i_read_only_list_envelope import LedgerTypeDtoIReadOnlyListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerTypeDtoIReadOnlyListEnvelope from a JSON string
ledger_type_dto_i_read_only_list_envelope_instance = LedgerTypeDtoIReadOnlyListEnvelope.from_json(json)
# print the JSON string representation of the object
print(LedgerTypeDtoIReadOnlyListEnvelope.to_json())

# convert the object into a dict
ledger_type_dto_i_read_only_list_envelope_dict = ledger_type_dto_i_read_only_list_envelope_instance.to_dict()
# create an instance of LedgerTypeDtoIReadOnlyListEnvelope from a dict
ledger_type_dto_i_read_only_list_envelope_from_dict = LedgerTypeDtoIReadOnlyListEnvelope.from_dict(ledger_type_dto_i_read_only_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



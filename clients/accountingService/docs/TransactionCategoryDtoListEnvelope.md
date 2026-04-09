# TransactionCategoryDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[TransactionCategoryDto]**](TransactionCategoryDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.transaction_category_dto_list_envelope import TransactionCategoryDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionCategoryDtoListEnvelope from a JSON string
transaction_category_dto_list_envelope_instance = TransactionCategoryDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(TransactionCategoryDtoListEnvelope.to_json())

# convert the object into a dict
transaction_category_dto_list_envelope_dict = transaction_category_dto_list_envelope_instance.to_dict()
# create an instance of TransactionCategoryDtoListEnvelope from a dict
transaction_category_dto_list_envelope_from_dict = TransactionCategoryDtoListEnvelope.from_dict(transaction_category_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



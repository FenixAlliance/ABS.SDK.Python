# TransactionCategoryDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**TransactionCategoryDto**](TransactionCategoryDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.transaction_category_dto_envelope import TransactionCategoryDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionCategoryDtoEnvelope from a JSON string
transaction_category_dto_envelope_instance = TransactionCategoryDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(TransactionCategoryDtoEnvelope.to_json())

# convert the object into a dict
transaction_category_dto_envelope_dict = transaction_category_dto_envelope_instance.to_dict()
# create an instance of TransactionCategoryDtoEnvelope from a dict
transaction_category_dto_envelope_from_dict = TransactionCategoryDtoEnvelope.from_dict(transaction_category_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DiscountDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**DiscountDto**](DiscountDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.discount_dto_envelope import DiscountDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountDtoEnvelope from a JSON string
discount_dto_envelope_instance = DiscountDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(DiscountDtoEnvelope.to_json())

# convert the object into a dict
discount_dto_envelope_dict = discount_dto_envelope_instance.to_dict()
# create an instance of DiscountDtoEnvelope from a dict
discount_dto_envelope_from_dict = DiscountDtoEnvelope.from_dict(discount_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DiscountListDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**DiscountListDto**](DiscountListDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.discount_list_dto_envelope import DiscountListDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountListDtoEnvelope from a JSON string
discount_list_dto_envelope_instance = DiscountListDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(DiscountListDtoEnvelope.to_json())

# convert the object into a dict
discount_list_dto_envelope_dict = discount_list_dto_envelope_instance.to_dict()
# create an instance of DiscountListDtoEnvelope from a dict
discount_list_dto_envelope_from_dict = DiscountListDtoEnvelope.from_dict(discount_list_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



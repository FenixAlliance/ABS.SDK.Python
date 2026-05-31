# BillOfLadingDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**BillOfLadingDto**](BillOfLadingDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.bill_of_lading_dto_envelope import BillOfLadingDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of BillOfLadingDtoEnvelope from a JSON string
bill_of_lading_dto_envelope_instance = BillOfLadingDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(BillOfLadingDtoEnvelope.to_json())

# convert the object into a dict
bill_of_lading_dto_envelope_dict = bill_of_lading_dto_envelope_instance.to_dict()
# create an instance of BillOfLadingDtoEnvelope from a dict
bill_of_lading_dto_envelope_from_dict = BillOfLadingDtoEnvelope.from_dict(bill_of_lading_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



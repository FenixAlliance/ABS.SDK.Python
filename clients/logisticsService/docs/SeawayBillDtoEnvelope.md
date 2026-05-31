# SeawayBillDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**SeawayBillDto**](SeawayBillDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.seaway_bill_dto_envelope import SeawayBillDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SeawayBillDtoEnvelope from a JSON string
seaway_bill_dto_envelope_instance = SeawayBillDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(SeawayBillDtoEnvelope.to_json())

# convert the object into a dict
seaway_bill_dto_envelope_dict = seaway_bill_dto_envelope_instance.to_dict()
# create an instance of SeawayBillDtoEnvelope from a dict
seaway_bill_dto_envelope_from_dict = SeawayBillDtoEnvelope.from_dict(seaway_bill_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



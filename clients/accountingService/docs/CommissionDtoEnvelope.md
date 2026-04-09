# CommissionDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**CommissionDto**](CommissionDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.commission_dto_envelope import CommissionDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionDtoEnvelope from a JSON string
commission_dto_envelope_instance = CommissionDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(CommissionDtoEnvelope.to_json())

# convert the object into a dict
commission_dto_envelope_dict = commission_dto_envelope_instance.to_dict()
# create an instance of CommissionDtoEnvelope from a dict
commission_dto_envelope_from_dict = CommissionDtoEnvelope.from_dict(commission_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



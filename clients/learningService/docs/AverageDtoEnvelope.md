# AverageDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**AverageDto**](AverageDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.average_dto_envelope import AverageDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AverageDtoEnvelope from a JSON string
average_dto_envelope_instance = AverageDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(AverageDtoEnvelope.to_json())

# convert the object into a dict
average_dto_envelope_dict = average_dto_envelope_instance.to_dict()
# create an instance of AverageDtoEnvelope from a dict
average_dto_envelope_from_dict = AverageDtoEnvelope.from_dict(average_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



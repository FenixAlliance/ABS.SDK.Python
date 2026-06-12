# ActivityTypeDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ActivityTypeDto**](ActivityTypeDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.activity_type_dto_envelope import ActivityTypeDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityTypeDtoEnvelope from a JSON string
activity_type_dto_envelope_instance = ActivityTypeDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ActivityTypeDtoEnvelope.to_json())

# convert the object into a dict
activity_type_dto_envelope_dict = activity_type_dto_envelope_instance.to_dict()
# create an instance of ActivityTypeDtoEnvelope from a dict
activity_type_dto_envelope_from_dict = ActivityTypeDtoEnvelope.from_dict(activity_type_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



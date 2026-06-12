# ActivityTypeDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ActivityTypeDto]**](ActivityTypeDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.activity_type_dto_list_envelope import ActivityTypeDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityTypeDtoListEnvelope from a JSON string
activity_type_dto_list_envelope_instance = ActivityTypeDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ActivityTypeDtoListEnvelope.to_json())

# convert the object into a dict
activity_type_dto_list_envelope_dict = activity_type_dto_list_envelope_instance.to_dict()
# create an instance of ActivityTypeDtoListEnvelope from a dict
activity_type_dto_list_envelope_from_dict = ActivityTypeDtoListEnvelope.from_dict(activity_type_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



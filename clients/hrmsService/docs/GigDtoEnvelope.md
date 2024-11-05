# GigDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**GigDto**](GigDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.gig_dto_envelope import GigDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of GigDtoEnvelope from a JSON string
gig_dto_envelope_instance = GigDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(GigDtoEnvelope.to_json())

# convert the object into a dict
gig_dto_envelope_dict = gig_dto_envelope_instance.to_dict()
# create an instance of GigDtoEnvelope from a dict
gig_dto_envelope_from_dict = GigDtoEnvelope.from_dict(gig_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



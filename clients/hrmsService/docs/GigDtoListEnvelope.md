# GigDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[GigDto]**](GigDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.gig_dto_list_envelope import GigDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of GigDtoListEnvelope from a JSON string
gig_dto_list_envelope_instance = GigDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(GigDtoListEnvelope.to_json())

# convert the object into a dict
gig_dto_list_envelope_dict = gig_dto_list_envelope_instance.to_dict()
# create an instance of GigDtoListEnvelope from a dict
gig_dto_list_envelope_from_dict = GigDtoListEnvelope.from_dict(gig_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


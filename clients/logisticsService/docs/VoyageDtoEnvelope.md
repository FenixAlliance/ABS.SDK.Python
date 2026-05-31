# VoyageDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**VoyageDto**](VoyageDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.voyage_dto_envelope import VoyageDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of VoyageDtoEnvelope from a JSON string
voyage_dto_envelope_instance = VoyageDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(VoyageDtoEnvelope.to_json())

# convert the object into a dict
voyage_dto_envelope_dict = voyage_dto_envelope_instance.to_dict()
# create an instance of VoyageDtoEnvelope from a dict
voyage_dto_envelope_from_dict = VoyageDtoEnvelope.from_dict(voyage_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



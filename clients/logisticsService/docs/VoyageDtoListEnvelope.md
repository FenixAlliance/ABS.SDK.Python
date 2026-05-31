# VoyageDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[VoyageDto]**](VoyageDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.voyage_dto_list_envelope import VoyageDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of VoyageDtoListEnvelope from a JSON string
voyage_dto_list_envelope_instance = VoyageDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(VoyageDtoListEnvelope.to_json())

# convert the object into a dict
voyage_dto_list_envelope_dict = voyage_dto_list_envelope_instance.to_dict()
# create an instance of VoyageDtoListEnvelope from a dict
voyage_dto_list_envelope_from_dict = VoyageDtoListEnvelope.from_dict(voyage_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



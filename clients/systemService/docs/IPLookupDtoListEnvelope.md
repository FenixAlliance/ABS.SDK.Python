# IPLookupDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[IPLookupDto]**](IPLookupDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.ip_lookup_dto_list_envelope import IPLookupDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of IPLookupDtoListEnvelope from a JSON string
ip_lookup_dto_list_envelope_instance = IPLookupDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(IPLookupDtoListEnvelope.to_json())

# convert the object into a dict
ip_lookup_dto_list_envelope_dict = ip_lookup_dto_list_envelope_instance.to_dict()
# create an instance of IPLookupDtoListEnvelope from a dict
ip_lookup_dto_list_envelope_from_dict = IPLookupDtoListEnvelope.from_dict(ip_lookup_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



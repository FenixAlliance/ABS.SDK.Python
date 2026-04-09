# TenantSegmentDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[TenantSegmentDto]**](TenantSegmentDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.tenant_segment_dto_list_envelope import TenantSegmentDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TenantSegmentDtoListEnvelope from a JSON string
tenant_segment_dto_list_envelope_instance = TenantSegmentDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(TenantSegmentDtoListEnvelope.to_json())

# convert the object into a dict
tenant_segment_dto_list_envelope_dict = tenant_segment_dto_list_envelope_instance.to_dict()
# create an instance of TenantSegmentDtoListEnvelope from a dict
tenant_segment_dto_list_envelope_from_dict = TenantSegmentDtoListEnvelope.from_dict(tenant_segment_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TenantSegmentDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**TenantSegmentDto**](TenantSegmentDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.tenant_segment_dto_envelope import TenantSegmentDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TenantSegmentDtoEnvelope from a JSON string
tenant_segment_dto_envelope_instance = TenantSegmentDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(TenantSegmentDtoEnvelope.to_json())

# convert the object into a dict
tenant_segment_dto_envelope_dict = tenant_segment_dto_envelope_instance.to_dict()
# create an instance of TenantSegmentDtoEnvelope from a dict
tenant_segment_dto_envelope_from_dict = TenantSegmentDtoEnvelope.from_dict(tenant_segment_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



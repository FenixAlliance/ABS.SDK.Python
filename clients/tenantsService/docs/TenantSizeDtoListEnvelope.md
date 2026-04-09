# TenantSizeDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[TenantSizeDto]**](TenantSizeDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.tenant_size_dto_list_envelope import TenantSizeDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TenantSizeDtoListEnvelope from a JSON string
tenant_size_dto_list_envelope_instance = TenantSizeDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(TenantSizeDtoListEnvelope.to_json())

# convert the object into a dict
tenant_size_dto_list_envelope_dict = tenant_size_dto_list_envelope_instance.to_dict()
# create an instance of TenantSizeDtoListEnvelope from a dict
tenant_size_dto_list_envelope_from_dict = TenantSizeDtoListEnvelope.from_dict(tenant_size_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



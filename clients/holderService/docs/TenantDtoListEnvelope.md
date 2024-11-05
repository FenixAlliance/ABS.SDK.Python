# TenantDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[TenantDto]**](TenantDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.tenant_dto_list_envelope import TenantDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDtoListEnvelope from a JSON string
tenant_dto_list_envelope_instance = TenantDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(TenantDtoListEnvelope.to_json())

# convert the object into a dict
tenant_dto_list_envelope_dict = tenant_dto_list_envelope_instance.to_dict()
# create an instance of TenantDtoListEnvelope from a dict
tenant_dto_list_envelope_from_dict = TenantDtoListEnvelope.from_dict(tenant_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TenantDepartmentDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[TenantDepartmentDto]**](TenantDepartmentDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.tenant_department_dto_list_envelope import TenantDepartmentDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDepartmentDtoListEnvelope from a JSON string
tenant_department_dto_list_envelope_instance = TenantDepartmentDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(TenantDepartmentDtoListEnvelope.to_json())

# convert the object into a dict
tenant_department_dto_list_envelope_dict = tenant_department_dto_list_envelope_instance.to_dict()
# create an instance of TenantDepartmentDtoListEnvelope from a dict
tenant_department_dto_list_envelope_from_dict = TenantDepartmentDtoListEnvelope.from_dict(tenant_department_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TenantUnitUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**business_unit_qualified_name** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**organization_profile_id** | **str** |  | [optional] 
**parent_business_unit_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_unit_update_dto import TenantUnitUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantUnitUpdateDto from a JSON string
tenant_unit_update_dto_instance = TenantUnitUpdateDto.from_json(json)
# print the JSON string representation of the object
print(TenantUnitUpdateDto.to_json())

# convert the object into a dict
tenant_unit_update_dto_dict = tenant_unit_update_dto_instance.to_dict()
# create an instance of TenantUnitUpdateDto from a dict
tenant_unit_update_dto_from_dict = TenantUnitUpdateDto.from_dict(tenant_unit_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



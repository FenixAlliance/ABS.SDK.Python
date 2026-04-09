# TenantPositionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**business_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_position_dto import TenantPositionDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantPositionDto from a JSON string
tenant_position_dto_instance = TenantPositionDto.from_json(json)
# print the JSON string representation of the object
print(TenantPositionDto.to_json())

# convert the object into a dict
tenant_position_dto_dict = tenant_position_dto_instance.to_dict()
# create an instance of TenantPositionDto from a dict
tenant_position_dto_from_dict = TenantPositionDto.from_dict(tenant_position_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



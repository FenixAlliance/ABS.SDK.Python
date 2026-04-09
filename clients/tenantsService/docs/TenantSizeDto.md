# TenantSizeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**employee_low_range_value** | **int** |  | [optional] 
**employee_high_range_value** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_size_dto import TenantSizeDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantSizeDto from a JSON string
tenant_size_dto_instance = TenantSizeDto.from_json(json)
# print the JSON string representation of the object
print(TenantSizeDto.to_json())

# convert the object into a dict
tenant_size_dto_dict = tenant_size_dto_instance.to_dict()
# create an instance of TenantSizeDto from a dict
tenant_size_dto_from_dict = TenantSizeDto.from_dict(tenant_size_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



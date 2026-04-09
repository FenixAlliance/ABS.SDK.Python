# TenantSizeUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**employee_low_range_value** | **int** |  | [optional] 
**employee_high_range_value** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_size_update_dto import TenantSizeUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantSizeUpdateDto from a JSON string
tenant_size_update_dto_instance = TenantSizeUpdateDto.from_json(json)
# print the JSON string representation of the object
print(TenantSizeUpdateDto.to_json())

# convert the object into a dict
tenant_size_update_dto_dict = tenant_size_update_dto_instance.to_dict()
# create an instance of TenantSizeUpdateDto from a dict
tenant_size_update_dto_from_dict = TenantSizeUpdateDto.from_dict(tenant_size_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



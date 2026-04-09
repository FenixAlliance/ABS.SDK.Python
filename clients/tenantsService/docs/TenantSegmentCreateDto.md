# TenantSegmentCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**revenue** | **str** |  | [optional] 
**min_employees** | **float** |  | [optional] 
**max_employees** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_segment_create_dto import TenantSegmentCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantSegmentCreateDto from a JSON string
tenant_segment_create_dto_instance = TenantSegmentCreateDto.from_json(json)
# print the JSON string representation of the object
print(TenantSegmentCreateDto.to_json())

# convert the object into a dict
tenant_segment_create_dto_dict = tenant_segment_create_dto_instance.to_dict()
# create an instance of TenantSegmentCreateDto from a dict
tenant_segment_create_dto_from_dict = TenantSegmentCreateDto.from_dict(tenant_segment_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



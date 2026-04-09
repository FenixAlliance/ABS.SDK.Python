# TenantTypeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_type_dto import TenantTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTypeDto from a JSON string
tenant_type_dto_instance = TenantTypeDto.from_json(json)
# print the JSON string representation of the object
print(TenantTypeDto.to_json())

# convert the object into a dict
tenant_type_dto_dict = tenant_type_dto_instance.to_dict()
# create an instance of TenantTypeDto from a dict
tenant_type_dto_from_dict = TenantTypeDto.from_dict(tenant_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



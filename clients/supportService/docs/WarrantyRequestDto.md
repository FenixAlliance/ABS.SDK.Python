# WarrantyRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**approved** | **bool** |  | [optional] 
**approved_timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**support_entitlement_id** | **str** |  | [optional] 
**contact_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**warranty_policy_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.warranty_request_dto import WarrantyRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of WarrantyRequestDto from a JSON string
warranty_request_dto_instance = WarrantyRequestDto.from_json(json)
# print the JSON string representation of the object
print(WarrantyRequestDto.to_json())

# convert the object into a dict
warranty_request_dto_dict = warranty_request_dto_instance.to_dict()
# create an instance of WarrantyRequestDto from a dict
warranty_request_dto_from_dict = WarrantyRequestDto.from_dict(warranty_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



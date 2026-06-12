# ReturnRequestDto


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
**return_policy_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.return_request_dto import ReturnRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnRequestDto from a JSON string
return_request_dto_instance = ReturnRequestDto.from_json(json)
# print the JSON string representation of the object
print(ReturnRequestDto.to_json())

# convert the object into a dict
return_request_dto_dict = return_request_dto_instance.to_dict()
# create an instance of ReturnRequestDto from a dict
return_request_dto_from_dict = ReturnRequestDto.from_dict(return_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



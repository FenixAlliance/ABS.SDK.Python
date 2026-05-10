# ReturnRequestUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**approved** | **bool** |  | [optional] 
**approved_timestamp** | **datetime** |  | [optional] 
**support_entitlement_id** | **str** |  | [optional] 
**return_policy_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.return_request_update_dto import ReturnRequestUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnRequestUpdateDto from a JSON string
return_request_update_dto_instance = ReturnRequestUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ReturnRequestUpdateDto.to_json())

# convert the object into a dict
return_request_update_dto_dict = return_request_update_dto_instance.to_dict()
# create an instance of ReturnRequestUpdateDto from a dict
return_request_update_dto_from_dict = ReturnRequestUpdateDto.from_dict(return_request_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



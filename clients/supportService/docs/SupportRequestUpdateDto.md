# SupportRequestUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**approved** | **bool** |  | [optional] 
**approved_timestamp** | **datetime** |  | [optional] 
**support_entitlement_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.support_request_update_dto import SupportRequestUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SupportRequestUpdateDto from a JSON string
support_request_update_dto_instance = SupportRequestUpdateDto.from_json(json)
# print the JSON string representation of the object
print(SupportRequestUpdateDto.to_json())

# convert the object into a dict
support_request_update_dto_dict = support_request_update_dto_instance.to_dict()
# create an instance of SupportRequestUpdateDto from a dict
support_request_update_dto_from_dict = SupportRequestUpdateDto.from_dict(support_request_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



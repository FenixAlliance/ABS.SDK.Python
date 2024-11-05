# SupportRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**approved** | **bool** |  | [optional] 
**approved_timestamp** | **datetime** |  | [optional] 
**business_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 
**support_entitlement_id** | **str** |  | [optional] 
**contact_id** | **str** |  | [optional] 
**account_holder_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.support_request_dto import SupportRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SupportRequestDto from a JSON string
support_request_dto_instance = SupportRequestDto.from_json(json)
# print the JSON string representation of the object
print(SupportRequestDto.to_json())

# convert the object into a dict
support_request_dto_dict = support_request_dto_instance.to_dict()
# create an instance of SupportRequestDto from a dict
support_request_dto_from_dict = SupportRequestDto.from_dict(support_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



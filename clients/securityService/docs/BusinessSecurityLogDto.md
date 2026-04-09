# BusinessSecurityLogDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**type** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**security_event** | **str** |  | [optional] 
**requires_attention** | **bool** |  | [optional] 
**business_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.business_security_log_dto import BusinessSecurityLogDto

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessSecurityLogDto from a JSON string
business_security_log_dto_instance = BusinessSecurityLogDto.from_json(json)
# print the JSON string representation of the object
print(BusinessSecurityLogDto.to_json())

# convert the object into a dict
business_security_log_dto_dict = business_security_log_dto_instance.to_dict()
# create an instance of BusinessSecurityLogDto from a dict
business_security_log_dto_from_dict = BusinessSecurityLogDto.from_dict(business_security_log_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



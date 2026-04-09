# BusinessSecurityLogDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[BusinessSecurityLogDto]**](BusinessSecurityLogDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.business_security_log_dto_list_envelope import BusinessSecurityLogDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessSecurityLogDtoListEnvelope from a JSON string
business_security_log_dto_list_envelope_instance = BusinessSecurityLogDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(BusinessSecurityLogDtoListEnvelope.to_json())

# convert the object into a dict
business_security_log_dto_list_envelope_dict = business_security_log_dto_list_envelope_instance.to_dict()
# create an instance of BusinessSecurityLogDtoListEnvelope from a dict
business_security_log_dto_list_envelope_from_dict = BusinessSecurityLogDtoListEnvelope.from_dict(business_security_log_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



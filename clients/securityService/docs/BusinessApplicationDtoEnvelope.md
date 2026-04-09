# BusinessApplicationDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**BusinessApplicationDto**](BusinessApplicationDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.business_application_dto_envelope import BusinessApplicationDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessApplicationDtoEnvelope from a JSON string
business_application_dto_envelope_instance = BusinessApplicationDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(BusinessApplicationDtoEnvelope.to_json())

# convert the object into a dict
business_application_dto_envelope_dict = business_application_dto_envelope_instance.to_dict()
# create an instance of BusinessApplicationDtoEnvelope from a dict
business_application_dto_envelope_from_dict = BusinessApplicationDtoEnvelope.from_dict(business_application_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



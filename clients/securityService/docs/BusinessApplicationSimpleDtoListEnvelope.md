# BusinessApplicationSimpleDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[BusinessApplicationSimpleDto]**](BusinessApplicationSimpleDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.business_application_simple_dto_list_envelope import BusinessApplicationSimpleDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessApplicationSimpleDtoListEnvelope from a JSON string
business_application_simple_dto_list_envelope_instance = BusinessApplicationSimpleDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(BusinessApplicationSimpleDtoListEnvelope.to_json())

# convert the object into a dict
business_application_simple_dto_list_envelope_dict = business_application_simple_dto_list_envelope_instance.to_dict()
# create an instance of BusinessApplicationSimpleDtoListEnvelope from a dict
business_application_simple_dto_list_envelope_from_dict = BusinessApplicationSimpleDtoListEnvelope.from_dict(business_application_simple_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



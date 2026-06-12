# BusinessDomainDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[BusinessDomainDto]**](BusinessDomainDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.business_domain_dto_list_envelope import BusinessDomainDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDomainDtoListEnvelope from a JSON string
business_domain_dto_list_envelope_instance = BusinessDomainDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(BusinessDomainDtoListEnvelope.to_json())

# convert the object into a dict
business_domain_dto_list_envelope_dict = business_domain_dto_list_envelope_instance.to_dict()
# create an instance of BusinessDomainDtoListEnvelope from a dict
business_domain_dto_list_envelope_from_dict = BusinessDomainDtoListEnvelope.from_dict(business_domain_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



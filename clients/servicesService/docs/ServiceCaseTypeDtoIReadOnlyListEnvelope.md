# ServiceCaseTypeDtoIReadOnlyListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ServiceCaseTypeDto]**](ServiceCaseTypeDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_case_type_dto_i_read_only_list_envelope import ServiceCaseTypeDtoIReadOnlyListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCaseTypeDtoIReadOnlyListEnvelope from a JSON string
service_case_type_dto_i_read_only_list_envelope_instance = ServiceCaseTypeDtoIReadOnlyListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ServiceCaseTypeDtoIReadOnlyListEnvelope.to_json())

# convert the object into a dict
service_case_type_dto_i_read_only_list_envelope_dict = service_case_type_dto_i_read_only_list_envelope_instance.to_dict()
# create an instance of ServiceCaseTypeDtoIReadOnlyListEnvelope from a dict
service_case_type_dto_i_read_only_list_envelope_from_dict = ServiceCaseTypeDtoIReadOnlyListEnvelope.from_dict(service_case_type_dto_i_read_only_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



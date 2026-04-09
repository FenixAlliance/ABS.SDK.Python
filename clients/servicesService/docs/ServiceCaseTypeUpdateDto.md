# ServiceCaseTypeUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_case_type_update_dto import ServiceCaseTypeUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCaseTypeUpdateDto from a JSON string
service_case_type_update_dto_instance = ServiceCaseTypeUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ServiceCaseTypeUpdateDto.to_json())

# convert the object into a dict
service_case_type_update_dto_dict = service_case_type_update_dto_instance.to_dict()
# create an instance of ServiceCaseTypeUpdateDto from a dict
service_case_type_update_dto_from_dict = ServiceCaseTypeUpdateDto.from_dict(service_case_type_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ServiceCaseTypeCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_case_type_create_dto import ServiceCaseTypeCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCaseTypeCreateDto from a JSON string
service_case_type_create_dto_instance = ServiceCaseTypeCreateDto.from_json(json)
# print the JSON string representation of the object
print(ServiceCaseTypeCreateDto.to_json())

# convert the object into a dict
service_case_type_create_dto_dict = service_case_type_create_dto_instance.to_dict()
# create an instance of ServiceCaseTypeCreateDto from a dict
service_case_type_create_dto_from_dict = ServiceCaseTypeCreateDto.from_dict(service_case_type_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



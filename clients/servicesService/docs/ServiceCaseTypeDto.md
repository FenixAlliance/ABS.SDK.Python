# ServiceCaseTypeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_case_type_dto import ServiceCaseTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCaseTypeDto from a JSON string
service_case_type_dto_instance = ServiceCaseTypeDto.from_json(json)
# print the JSON string representation of the object
print(ServiceCaseTypeDto.to_json())

# convert the object into a dict
service_case_type_dto_dict = service_case_type_dto_instance.to_dict()
# create an instance of ServiceCaseTypeDto from a dict
service_case_type_dto_from_dict = ServiceCaseTypeDto.from_dict(service_case_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



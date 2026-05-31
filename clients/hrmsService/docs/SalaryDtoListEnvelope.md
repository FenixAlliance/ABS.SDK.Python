# SalaryDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[SalaryDto]**](SalaryDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.salary_dto_list_envelope import SalaryDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SalaryDtoListEnvelope from a JSON string
salary_dto_list_envelope_instance = SalaryDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(SalaryDtoListEnvelope.to_json())

# convert the object into a dict
salary_dto_list_envelope_dict = salary_dto_list_envelope_instance.to_dict()
# create an instance of SalaryDtoListEnvelope from a dict
salary_dto_list_envelope_from_dict = SalaryDtoListEnvelope.from_dict(salary_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



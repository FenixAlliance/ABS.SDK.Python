# FiscalResponsibilityRecordDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**fiscal_responsibility_id** | **str** |  | [optional] 
**billing_profile_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.fiscal_responsibility_record_dto import FiscalResponsibilityRecordDto

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalResponsibilityRecordDto from a JSON string
fiscal_responsibility_record_dto_instance = FiscalResponsibilityRecordDto.from_json(json)
# print the JSON string representation of the object
print(FiscalResponsibilityRecordDto.to_json())

# convert the object into a dict
fiscal_responsibility_record_dto_dict = fiscal_responsibility_record_dto_instance.to_dict()
# create an instance of FiscalResponsibilityRecordDto from a dict
fiscal_responsibility_record_dto_from_dict = FiscalResponsibilityRecordDto.from_dict(fiscal_responsibility_record_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



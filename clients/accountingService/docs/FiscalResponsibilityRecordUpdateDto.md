# FiscalResponsibilityRecordUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fiscal_responsibility_id** | **str** |  | [optional] 
**billing_profile_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.fiscal_responsibility_record_update_dto import FiscalResponsibilityRecordUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalResponsibilityRecordUpdateDto from a JSON string
fiscal_responsibility_record_update_dto_instance = FiscalResponsibilityRecordUpdateDto.from_json(json)
# print the JSON string representation of the object
print(FiscalResponsibilityRecordUpdateDto.to_json())

# convert the object into a dict
fiscal_responsibility_record_update_dto_dict = fiscal_responsibility_record_update_dto_instance.to_dict()
# create an instance of FiscalResponsibilityRecordUpdateDto from a dict
fiscal_responsibility_record_update_dto_from_dict = FiscalResponsibilityRecordUpdateDto.from_dict(fiscal_responsibility_record_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



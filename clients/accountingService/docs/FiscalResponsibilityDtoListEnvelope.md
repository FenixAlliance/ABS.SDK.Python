# FiscalResponsibilityDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[FiscalResponsibilityDto]**](FiscalResponsibilityDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.fiscal_responsibility_dto_list_envelope import FiscalResponsibilityDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalResponsibilityDtoListEnvelope from a JSON string
fiscal_responsibility_dto_list_envelope_instance = FiscalResponsibilityDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(FiscalResponsibilityDtoListEnvelope.to_json())

# convert the object into a dict
fiscal_responsibility_dto_list_envelope_dict = fiscal_responsibility_dto_list_envelope_instance.to_dict()
# create an instance of FiscalResponsibilityDtoListEnvelope from a dict
fiscal_responsibility_dto_list_envelope_from_dict = FiscalResponsibilityDtoListEnvelope.from_dict(fiscal_responsibility_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# FiscalIdentificationTypeDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**FiscalIdentificationTypeDto**](FiscalIdentificationTypeDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.fiscal_identification_type_dto_envelope import FiscalIdentificationTypeDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalIdentificationTypeDtoEnvelope from a JSON string
fiscal_identification_type_dto_envelope_instance = FiscalIdentificationTypeDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(FiscalIdentificationTypeDtoEnvelope.to_json())

# convert the object into a dict
fiscal_identification_type_dto_envelope_dict = fiscal_identification_type_dto_envelope_instance.to_dict()
# create an instance of FiscalIdentificationTypeDtoEnvelope from a dict
fiscal_identification_type_dto_envelope_from_dict = FiscalIdentificationTypeDtoEnvelope.from_dict(fiscal_identification_type_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



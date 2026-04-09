# FiscalAuthorityDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[FiscalAuthorityDto]**](FiscalAuthorityDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.fiscal_authority_dto_list_envelope import FiscalAuthorityDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalAuthorityDtoListEnvelope from a JSON string
fiscal_authority_dto_list_envelope_instance = FiscalAuthorityDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(FiscalAuthorityDtoListEnvelope.to_json())

# convert the object into a dict
fiscal_authority_dto_list_envelope_dict = fiscal_authority_dto_list_envelope_instance.to_dict()
# create an instance of FiscalAuthorityDtoListEnvelope from a dict
fiscal_authority_dto_list_envelope_from_dict = FiscalAuthorityDtoListEnvelope.from_dict(fiscal_authority_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



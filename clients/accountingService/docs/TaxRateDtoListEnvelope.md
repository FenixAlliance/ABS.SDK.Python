# TaxRateDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[TaxRateDto]**](TaxRateDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.tax_rate_dto_list_envelope import TaxRateDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TaxRateDtoListEnvelope from a JSON string
tax_rate_dto_list_envelope_instance = TaxRateDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(TaxRateDtoListEnvelope.to_json())

# convert the object into a dict
tax_rate_dto_list_envelope_dict = tax_rate_dto_list_envelope_instance.to_dict()
# create an instance of TaxRateDtoListEnvelope from a dict
tax_rate_dto_list_envelope_from_dict = TaxRateDtoListEnvelope.from_dict(tax_rate_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



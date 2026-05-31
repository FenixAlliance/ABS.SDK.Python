# TaxClassDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[TaxClassDto]**](TaxClassDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.tax_class_dto_list_envelope import TaxClassDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TaxClassDtoListEnvelope from a JSON string
tax_class_dto_list_envelope_instance = TaxClassDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(TaxClassDtoListEnvelope.to_json())

# convert the object into a dict
tax_class_dto_list_envelope_dict = tax_class_dto_list_envelope_instance.to_dict()
# create an instance of TaxClassDtoListEnvelope from a dict
tax_class_dto_list_envelope_from_dict = TaxClassDtoListEnvelope.from_dict(tax_class_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



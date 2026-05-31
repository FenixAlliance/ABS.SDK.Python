# TaxClassUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**fiscal_authority_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tax_class_update_dto import TaxClassUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TaxClassUpdateDto from a JSON string
tax_class_update_dto_instance = TaxClassUpdateDto.from_json(json)
# print the JSON string representation of the object
print(TaxClassUpdateDto.to_json())

# convert the object into a dict
tax_class_update_dto_dict = tax_class_update_dto_instance.to_dict()
# create an instance of TaxClassUpdateDto from a dict
tax_class_update_dto_from_dict = TaxClassUpdateDto.from_dict(tax_class_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



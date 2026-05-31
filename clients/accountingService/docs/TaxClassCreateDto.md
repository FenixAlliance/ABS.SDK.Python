# TaxClassCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**fiscal_authority_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tax_class_create_dto import TaxClassCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TaxClassCreateDto from a JSON string
tax_class_create_dto_instance = TaxClassCreateDto.from_json(json)
# print the JSON string representation of the object
print(TaxClassCreateDto.to_json())

# convert the object into a dict
tax_class_create_dto_dict = tax_class_create_dto_instance.to_dict()
# create an instance of TaxClassCreateDto from a dict
tax_class_create_dto_from_dict = TaxClassCreateDto.from_dict(tax_class_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



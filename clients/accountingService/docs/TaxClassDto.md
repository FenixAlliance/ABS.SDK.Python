# TaxClassDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**fiscal_authority_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tax_class_dto import TaxClassDto

# TODO update the JSON string below
json = "{}"
# create an instance of TaxClassDto from a JSON string
tax_class_dto_instance = TaxClassDto.from_json(json)
# print the JSON string representation of the object
print(TaxClassDto.to_json())

# convert the object into a dict
tax_class_dto_dict = tax_class_dto_instance.to_dict()
# create an instance of TaxClassDto from a dict
tax_class_dto_from_dict = TaxClassDto.from_dict(tax_class_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



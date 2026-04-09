# InvoiceEnumerationRangeCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**prefix** | **str** |  | [optional] 
**suffix** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 
**qualified_name** | **str** |  | [optional] 
**current_numeration** | **int** |  | [optional] 
**numeration_from** | **int** |  | [optional] 
**numeration_to** | **int** |  | [optional] 
**valid_from** | **datetime** |  | 
**valid_to** | **datetime** |  | 
**fiscal_authority_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**document_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.invoice_enumeration_range_create_dto import InvoiceEnumerationRangeCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceEnumerationRangeCreateDto from a JSON string
invoice_enumeration_range_create_dto_instance = InvoiceEnumerationRangeCreateDto.from_json(json)
# print the JSON string representation of the object
print(InvoiceEnumerationRangeCreateDto.to_json())

# convert the object into a dict
invoice_enumeration_range_create_dto_dict = invoice_enumeration_range_create_dto_instance.to_dict()
# create an instance of InvoiceEnumerationRangeCreateDto from a dict
invoice_enumeration_range_create_dto_from_dict = InvoiceEnumerationRangeCreateDto.from_dict(invoice_enumeration_range_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



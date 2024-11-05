# InvoiceLineCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**invoice_id** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**item_id** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.invoice_line_create_dto import InvoiceLineCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceLineCreateDto from a JSON string
invoice_line_create_dto_instance = InvoiceLineCreateDto.from_json(json)
# print the JSON string representation of the object
print(InvoiceLineCreateDto.to_json())

# convert the object into a dict
invoice_line_create_dto_dict = invoice_line_create_dto_instance.to_dict()
# create an instance of InvoiceLineCreateDto from a dict
invoice_line_create_dto_from_dict = InvoiceLineCreateDto.from_dict(invoice_line_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



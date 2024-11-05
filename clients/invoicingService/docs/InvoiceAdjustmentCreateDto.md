# InvoiceAdjustmentCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**tenant_id** | **str** |  | [optional] 
**invoice_id** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**surcharge_percent** | **float** |  | [optional] 
**surcharge_amount** | **float** |  | [optional] 
**discount_percent** | **float** |  | [optional] 
**discount_amount** | **float** |  | [optional] 
**total_surcharge** | **float** |  | [optional] 
**total_discount** | **float** |  | [optional] 
**type** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.invoice_adjustment_create_dto import InvoiceAdjustmentCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceAdjustmentCreateDto from a JSON string
invoice_adjustment_create_dto_instance = InvoiceAdjustmentCreateDto.from_json(json)
# print the JSON string representation of the object
print(InvoiceAdjustmentCreateDto.to_json())

# convert the object into a dict
invoice_adjustment_create_dto_dict = invoice_adjustment_create_dto_instance.to_dict()
# create an instance of InvoiceAdjustmentCreateDto from a dict
invoice_adjustment_create_dto_from_dict = InvoiceAdjustmentCreateDto.from_dict(invoice_adjustment_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



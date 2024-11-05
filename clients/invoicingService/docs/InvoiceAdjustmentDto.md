# InvoiceAdjustmentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
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
from openapi_client.models.invoice_adjustment_dto import InvoiceAdjustmentDto

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceAdjustmentDto from a JSON string
invoice_adjustment_dto_instance = InvoiceAdjustmentDto.from_json(json)
# print the JSON string representation of the object
print(InvoiceAdjustmentDto.to_json())

# convert the object into a dict
invoice_adjustment_dto_dict = invoice_adjustment_dto_instance.to_dict()
# create an instance of InvoiceAdjustmentDto from a dict
invoice_adjustment_dto_from_dict = InvoiceAdjustmentDto.from_dict(invoice_adjustment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InvoiceCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**closed** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**price_list_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**individual_id** | **str** |  | [optional] 
**payment_term_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**forex_rate** | **float** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**billing_email** | **str** |  | [optional] 
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**state_id** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 
**paid** | **bool** |  | [optional] 
**number** | **int** |  | [optional] 
**notes** | **str** |  | [optional] 
**customer_notes** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**enumeration** | **str** |  | [optional] 
**payment_mode_id** | **str** |  | [optional] 
**receiver_tenant_id** | **str** |  | [optional] 
**enumeration_range_id** | **str** |  | [optional] 
**emisor_billing_profile_id** | **str** |  | [optional] 
**receiver_billing_profile_id** | **str** |  | [optional] 
**emisor_wallet_account_id** | **str** |  | [optional] 
**receiver_wallet_account_id** | **str** |  | [optional] 
**payment_due** | **datetime** |  | [optional] 
**invoice_type** | **int** |  | [optional] 
**document_type** | **int** |  | [optional] 
**invoice_status** | **int** |  | [optional] 
**valid_from** | **datetime** |  | [optional] 
**valid_to** | **datetime** |  | [optional] 
**invoice_references** | [**List[InvoiceReferenceDto]**](InvoiceReferenceDto.md) |  | [optional] 
**invoice_item_records** | [**List[InvoiceItemRecordDto]**](InvoiceItemRecordDto.md) |  | [optional] 
**invoice_adjustments** | [**List[InvoiceAdjustmentDto]**](InvoiceAdjustmentDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.invoice_create_dto import InvoiceCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceCreateDto from a JSON string
invoice_create_dto_instance = InvoiceCreateDto.from_json(json)
# print the JSON string representation of the object
print(InvoiceCreateDto.to_json())

# convert the object into a dict
invoice_create_dto_dict = invoice_create_dto_instance.to_dict()
# create an instance of InvoiceCreateDto from a dict
invoice_create_dto_from_dict = InvoiceCreateDto.from_dict(invoice_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ReceiptUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**forex_rate** | **float** |  | [optional] 
**total_amount** | **float** |  | [optional] 
**total_amount_in_usd** | **float** |  | [optional] 
**closed** | **bool** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**account_holder_id** | **str** |  | [optional] 
**contact_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**invoice_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.receipt_update_dto import ReceiptUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiptUpdateDto from a JSON string
receipt_update_dto_instance = ReceiptUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ReceiptUpdateDto.to_json())

# convert the object into a dict
receipt_update_dto_dict = receipt_update_dto_instance.to_dict()
# create an instance of ReceiptUpdateDto from a dict
receipt_update_dto_from_dict = ReceiptUpdateDto.from_dict(receipt_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



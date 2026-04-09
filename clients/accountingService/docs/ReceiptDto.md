# ReceiptDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**payment_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**closed** | **bool** |  | [optional] 
**account_holder_id** | **str** |  | [optional] 
**contact_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**receipt_type** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**invoice_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.receipt_dto import ReceiptDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiptDto from a JSON string
receipt_dto_instance = ReceiptDto.from_json(json)
# print the JSON string representation of the object
print(ReceiptDto.to_json())

# convert the object into a dict
receipt_dto_dict = receipt_dto_instance.to_dict()
# create an instance of ReceiptDto from a dict
receipt_dto_from_dict = ReceiptDto.from_dict(receipt_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



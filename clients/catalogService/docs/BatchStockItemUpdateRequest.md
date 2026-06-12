# BatchStockItemUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_ids** | **List[str]** |  | [optional] 
**published** | **bool** |  | [optional] 
**taxable** | **bool** |  | [optional] 
**add_tax_policy_ids** | **List[str]** |  | [optional] 
**remove_tax_policy_ids** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.batch_stock_item_update_request import BatchStockItemUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchStockItemUpdateRequest from a JSON string
batch_stock_item_update_request_instance = BatchStockItemUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(BatchStockItemUpdateRequest.to_json())

# convert the object into a dict
batch_stock_item_update_request_dict = batch_stock_item_update_request_instance.to_dict()
# create an instance of BatchStockItemUpdateRequest from a dict
batch_stock_item_update_request_from_dict = BatchStockItemUpdateRequest.from_dict(batch_stock_item_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InventoryOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_stock_management** | **bool** |  | [optional] 
**hide_out_of_stock_products** | **bool** |  | [optional] 
**enable_low_stock_notifications** | **bool** |  | [optional] 
**enable_out_of_stock_notifications** | **bool** |  | [optional] 
**stock_notification_recipients** | **str** |  | [optional] 
**hold_stock** | **int** |  | [optional] 
**low_stock_threshold** | **int** |  | [optional] 
**out_of_stock_threshold** | **int** |  | [optional] 
**stock_display_format** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.inventory_options import InventoryOptions

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryOptions from a JSON string
inventory_options_instance = InventoryOptions.from_json(json)
# print the JSON string representation of the object
print(InventoryOptions.to_json())

# convert the object into a dict
inventory_options_dict = inventory_options_instance.to_dict()
# create an instance of InventoryOptions from a dict
inventory_options_from_dict = InventoryOptions.from_dict(inventory_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



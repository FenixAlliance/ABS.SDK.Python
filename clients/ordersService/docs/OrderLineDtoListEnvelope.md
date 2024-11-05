# OrderLineDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[OrderLineDto]**](OrderLineDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.order_line_dto_list_envelope import OrderLineDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of OrderLineDtoListEnvelope from a JSON string
order_line_dto_list_envelope_instance = OrderLineDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(OrderLineDtoListEnvelope.to_json())

# convert the object into a dict
order_line_dto_list_envelope_dict = order_line_dto_list_envelope_instance.to_dict()
# create an instance of OrderLineDtoListEnvelope from a dict
order_line_dto_list_envelope_from_dict = OrderLineDtoListEnvelope.from_dict(order_line_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



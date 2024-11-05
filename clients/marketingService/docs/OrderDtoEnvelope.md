# OrderDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**OrderDto**](OrderDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.order_dto_envelope import OrderDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDtoEnvelope from a JSON string
order_dto_envelope_instance = OrderDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(OrderDtoEnvelope.to_json())

# convert the object into a dict
order_dto_envelope_dict = order_dto_envelope_instance.to_dict()
# create an instance of OrderDtoEnvelope from a dict
order_dto_envelope_from_dict = OrderDtoEnvelope.from_dict(order_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



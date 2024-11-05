# OrderDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[OrderDto]**](OrderDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.order_dto_list_envelope import OrderDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDtoListEnvelope from a JSON string
order_dto_list_envelope_instance = OrderDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(OrderDtoListEnvelope.to_json())

# convert the object into a dict
order_dto_list_envelope_dict = order_dto_list_envelope_instance.to_dict()
# create an instance of OrderDtoListEnvelope from a dict
order_dto_list_envelope_from_dict = OrderDtoListEnvelope.from_dict(order_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



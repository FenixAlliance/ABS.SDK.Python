# WaybillLineDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[WaybillLineDto]**](WaybillLineDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.waybill_line_dto_list_envelope import WaybillLineDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of WaybillLineDtoListEnvelope from a JSON string
waybill_line_dto_list_envelope_instance = WaybillLineDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(WaybillLineDtoListEnvelope.to_json())

# convert the object into a dict
waybill_line_dto_list_envelope_dict = waybill_line_dto_list_envelope_instance.to_dict()
# create an instance of WaybillLineDtoListEnvelope from a dict
waybill_line_dto_list_envelope_from_dict = WaybillLineDtoListEnvelope.from_dict(waybill_line_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



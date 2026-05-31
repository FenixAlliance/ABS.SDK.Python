# BillOfLadingLineDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[BillOfLadingLineDto]**](BillOfLadingLineDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.bill_of_lading_line_dto_list_envelope import BillOfLadingLineDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of BillOfLadingLineDtoListEnvelope from a JSON string
bill_of_lading_line_dto_list_envelope_instance = BillOfLadingLineDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(BillOfLadingLineDtoListEnvelope.to_json())

# convert the object into a dict
bill_of_lading_line_dto_list_envelope_dict = bill_of_lading_line_dto_list_envelope_instance.to_dict()
# create an instance of BillOfLadingLineDtoListEnvelope from a dict
bill_of_lading_line_dto_list_envelope_from_dict = BillOfLadingLineDtoListEnvelope.from_dict(bill_of_lading_line_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



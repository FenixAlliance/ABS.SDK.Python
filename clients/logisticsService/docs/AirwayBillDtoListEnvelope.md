# AirwayBillDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[AirwayBillDto]**](AirwayBillDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.airway_bill_dto_list_envelope import AirwayBillDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AirwayBillDtoListEnvelope from a JSON string
airway_bill_dto_list_envelope_instance = AirwayBillDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(AirwayBillDtoListEnvelope.to_json())

# convert the object into a dict
airway_bill_dto_list_envelope_dict = airway_bill_dto_list_envelope_instance.to_dict()
# create an instance of AirwayBillDtoListEnvelope from a dict
airway_bill_dto_list_envelope_from_dict = AirwayBillDtoListEnvelope.from_dict(airway_bill_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



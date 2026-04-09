# CommissionDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[CommissionDto]**](CommissionDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.commission_dto_list_envelope import CommissionDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionDtoListEnvelope from a JSON string
commission_dto_list_envelope_instance = CommissionDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(CommissionDtoListEnvelope.to_json())

# convert the object into a dict
commission_dto_list_envelope_dict = commission_dto_list_envelope_instance.to_dict()
# create an instance of CommissionDtoListEnvelope from a dict
commission_dto_list_envelope_from_dict = CommissionDtoListEnvelope.from_dict(commission_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



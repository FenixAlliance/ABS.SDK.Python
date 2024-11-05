# CityDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[CityDto]**](CityDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.city_dto_list_envelope import CityDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CityDtoListEnvelope from a JSON string
city_dto_list_envelope_instance = CityDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(CityDtoListEnvelope.to_json())

# convert the object into a dict
city_dto_list_envelope_dict = city_dto_list_envelope_instance.to_dict()
# create an instance of CityDtoListEnvelope from a dict
city_dto_list_envelope_from_dict = CityDtoListEnvelope.from_dict(city_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CityDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**state_id** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**latitude** | **str** |  | [optional] 
**longitude** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.city_dto import CityDto

# TODO update the JSON string below
json = "{}"
# create an instance of CityDto from a JSON string
city_dto_instance = CityDto.from_json(json)
# print the JSON string representation of the object
print(CityDto.to_json())

# convert the object into a dict
city_dto_dict = city_dto_instance.to_dict()
# create an instance of CityDto from a dict
city_dto_from_dict = CityDto.from_dict(city_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# VoyageCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**voyage_number** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**voyage_direction** | **str** |  | [optional] 
**departure_date** | **datetime** |  | [optional] 
**arrival_date** | **datetime** |  | [optional] 
**vessel_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.voyage_create_dto import VoyageCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of VoyageCreateDto from a JSON string
voyage_create_dto_instance = VoyageCreateDto.from_json(json)
# print the JSON string representation of the object
print(VoyageCreateDto.to_json())

# convert the object into a dict
voyage_create_dto_dict = voyage_create_dto_instance.to_dict()
# create an instance of VoyageCreateDto from a dict
voyage_create_dto_from_dict = VoyageCreateDto.from_dict(voyage_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



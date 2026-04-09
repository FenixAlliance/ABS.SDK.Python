# AverageDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**average** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.average_dto import AverageDto

# TODO update the JSON string below
json = "{}"
# create an instance of AverageDto from a JSON string
average_dto_instance = AverageDto.from_json(json)
# print the JSON string representation of the object
print(AverageDto.to_json())

# convert the object into a dict
average_dto_dict = average_dto_instance.to_dict()
# create an instance of AverageDto from a dict
average_dto_from_dict = AverageDto.from_dict(average_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



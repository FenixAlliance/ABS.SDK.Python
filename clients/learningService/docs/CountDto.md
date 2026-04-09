# CountDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.count_dto import CountDto

# TODO update the JSON string below
json = "{}"
# create an instance of CountDto from a JSON string
count_dto_instance = CountDto.from_json(json)
# print the JSON string representation of the object
print(CountDto.to_json())

# convert the object into a dict
count_dto_dict = count_dto_instance.to_dict()
# create an instance of CountDto from a dict
count_dto_from_dict = CountDto.from_dict(count_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



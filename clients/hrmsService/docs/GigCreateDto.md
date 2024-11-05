# GigCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.gig_create_dto import GigCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of GigCreateDto from a JSON string
gig_create_dto_instance = GigCreateDto.from_json(json)
# print the JSON string representation of the object
print(GigCreateDto.to_json())

# convert the object into a dict
gig_create_dto_dict = gig_create_dto_instance.to_dict()
# create an instance of GigCreateDto from a dict
gig_create_dto_from_dict = GigCreateDto.from_dict(gig_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



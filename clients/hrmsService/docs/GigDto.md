# GigDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.gig_dto import GigDto

# TODO update the JSON string below
json = "{}"
# create an instance of GigDto from a JSON string
gig_dto_instance = GigDto.from_json(json)
# print the JSON string representation of the object
print(GigDto.to_json())

# convert the object into a dict
gig_dto_dict = gig_dto_instance.to_dict()
# create an instance of GigDto from a dict
gig_dto_from_dict = GigDto.from_dict(gig_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



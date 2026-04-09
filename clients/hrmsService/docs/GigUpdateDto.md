# GigUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**category** | **str** |  | [optional] 
**tags** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.gig_update_dto import GigUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of GigUpdateDto from a JSON string
gig_update_dto_instance = GigUpdateDto.from_json(json)
# print the JSON string representation of the object
print(GigUpdateDto.to_json())

# convert the object into a dict
gig_update_dto_dict = gig_update_dto_instance.to_dict()
# create an instance of GigUpdateDto from a dict
gig_update_dto_from_dict = GigUpdateDto.from_dict(gig_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



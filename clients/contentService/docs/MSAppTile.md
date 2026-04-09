# MSAppTile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**logo_square** | **str** |  | [optional] 
**logo144** | **str** |  | [optional] 
**logo150** | **str** |  | [optional] 
**logo310** | **str** |  | [optional] 
**logo310_w** | **str** |  | [optional] 
**logo70** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ms_app_tile import MSAppTile

# TODO update the JSON string below
json = "{}"
# create an instance of MSAppTile from a JSON string
ms_app_tile_instance = MSAppTile.from_json(json)
# print the JSON string representation of the object
print(MSAppTile.to_json())

# convert the object into a dict
ms_app_tile_dict = ms_app_tile_instance.to_dict()
# create an instance of MSAppTile from a dict
ms_app_tile_from_dict = MSAppTile.from_dict(ms_app_tile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



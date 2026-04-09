# Favicons


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favicon** | **str** |  | [optional] 
**favicon16** | **str** |  | [optional] 
**favicon32** | **str** |  | [optional] 
**favicon96** | **str** |  | [optional] 
**favicon128** | **str** |  | [optional] 
**favicon196** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.favicons import Favicons

# TODO update the JSON string below
json = "{}"
# create an instance of Favicons from a JSON string
favicons_instance = Favicons.from_json(json)
# print the JSON string representation of the object
print(Favicons.to_json())

# convert the object into a dict
favicons_dict = favicons_instance.to_dict()
# create an instance of Favicons from a dict
favicons_from_dict = Favicons.from_dict(favicons_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



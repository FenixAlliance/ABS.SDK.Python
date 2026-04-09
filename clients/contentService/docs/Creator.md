# Creator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**organization** | **str** |  | [optional] 
**twitter_handler** | **str** |  | [optional] 
**git_hub_username** | **str** |  | [optional] 
**facebook_username** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.creator import Creator

# TODO update the JSON string below
json = "{}"
# create an instance of Creator from a JSON string
creator_instance = Creator.from_json(json)
# print the JSON string representation of the object
print(Creator.to_json())

# convert the object into a dict
creator_dict = creator_instance.to_dict()
# create an instance of Creator from a dict
creator_from_dict = Creator.from_dict(creator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



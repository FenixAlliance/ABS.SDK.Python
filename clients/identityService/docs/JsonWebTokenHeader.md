# JsonWebTokenHeader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** |  | [optional] 
**jku** | **str** |  | [optional] 
**kid** | **str** |  | [optional] 
**typ** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.json_web_token_header import JsonWebTokenHeader

# TODO update the JSON string below
json = "{}"
# create an instance of JsonWebTokenHeader from a JSON string
json_web_token_header_instance = JsonWebTokenHeader.from_json(json)
# print the JSON string representation of the object
print(JsonWebTokenHeader.to_json())

# convert the object into a dict
json_web_token_header_dict = json_web_token_header_instance.to_dict()
# create an instance of JsonWebTokenHeader from a dict
json_web_token_header_from_dict = JsonWebTokenHeader.from_dict(json_web_token_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



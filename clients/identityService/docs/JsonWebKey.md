# JsonWebKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kid** | **str** |  | [optional] 
**nbf** | **int** |  | [optional] 
**use** | **str** |  | [optional] 
**kty** | **str** |  | [optional] 
**e** | **str** |  | [optional] 
**n** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.json_web_key import JsonWebKey

# TODO update the JSON string below
json = "{}"
# create an instance of JsonWebKey from a JSON string
json_web_key_instance = JsonWebKey.from_json(json)
# print the JSON string representation of the object
print(JsonWebKey.to_json())

# convert the object into a dict
json_web_key_dict = json_web_key_instance.to_dict()
# create an instance of JsonWebKey from a dict
json_web_key_from_dict = JsonWebKey.from_dict(json_web_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



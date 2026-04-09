# JsonWebToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | [**JsonWebTokenHeader**](JsonWebTokenHeader.md) |  | [optional] 
**payload** | [**JsonWebTokenPayload**](JsonWebTokenPayload.md) |  | [optional] 
**signature** | **str** |  | [optional] 
**token_type** | **str** |  | [optional] 
**expires_in** | **int** |  | [optional] 
**access_token** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.json_web_token import JsonWebToken

# TODO update the JSON string below
json = "{}"
# create an instance of JsonWebToken from a JSON string
json_web_token_instance = JsonWebToken.from_json(json)
# print the JSON string representation of the object
print(JsonWebToken.to_json())

# convert the object into a dict
json_web_token_dict = json_web_token_instance.to_dict()
# create an instance of JsonWebToken from a dict
json_web_token_from_dict = JsonWebToken.from_dict(json_web_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



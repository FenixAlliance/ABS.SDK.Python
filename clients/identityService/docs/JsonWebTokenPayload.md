# JsonWebTokenPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aud** | **str** |  | [optional] 
**cid** | **str** |  | [optional] 
**iss** | **str** |  | [optional] 
**aid** | **str** |  | [optional] 
**sub** | **str** |  | [optional] 
**act** | **str** |  | [optional] 
**iat** | **int** |  | [optional] 
**nbf** | **int** |  | [optional] 
**exp** | **int** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.json_web_token_payload import JsonWebTokenPayload

# TODO update the JSON string below
json = "{}"
# create an instance of JsonWebTokenPayload from a JSON string
json_web_token_payload_instance = JsonWebTokenPayload.from_json(json)
# print the JSON string representation of the object
print(JsonWebTokenPayload.to_json())

# convert the object into a dict
json_web_token_payload_dict = json_web_token_payload_instance.to_dict()
# create an instance of JsonWebTokenPayload from a dict
json_web_token_payload_from_dict = JsonWebTokenPayload.from_dict(json_web_token_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



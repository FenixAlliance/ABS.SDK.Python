# ISwaggerEndpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.i_swagger_endpoint import ISwaggerEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of ISwaggerEndpoint from a JSON string
i_swagger_endpoint_instance = ISwaggerEndpoint.from_json(json)
# print the JSON string representation of the object
print(ISwaggerEndpoint.to_json())

# convert the object into a dict
i_swagger_endpoint_dict = i_swagger_endpoint_instance.to_dict()
# create an instance of ISwaggerEndpoint from a dict
i_swagger_endpoint_from_dict = ISwaggerEndpoint.from_dict(i_swagger_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



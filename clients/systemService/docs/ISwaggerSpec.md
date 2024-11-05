# ISwaggerSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**terms_of_service** | **str** |  | [optional] 
**swagger_endpoint** | [**ISwaggerEndpoint**](ISwaggerEndpoint.md) |  | [optional] 
**open_api_contact** | [**ISwaggerContact**](ISwaggerContact.md) |  | [optional] 
**license** | [**ISwaggerLicense**](ISwaggerLicense.md) |  | [optional] 

## Example

```python
from openapi_client.models.i_swagger_spec import ISwaggerSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ISwaggerSpec from a JSON string
i_swagger_spec_instance = ISwaggerSpec.from_json(json)
# print the JSON string representation of the object
print(ISwaggerSpec.to_json())

# convert the object into a dict
i_swagger_spec_dict = i_swagger_spec_instance.to_dict()
# create an instance of ISwaggerSpec from a dict
i_swagger_spec_from_dict = ISwaggerSpec.from_dict(i_swagger_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



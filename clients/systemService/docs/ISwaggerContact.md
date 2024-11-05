# ISwaggerContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.i_swagger_contact import ISwaggerContact

# TODO update the JSON string below
json = "{}"
# create an instance of ISwaggerContact from a JSON string
i_swagger_contact_instance = ISwaggerContact.from_json(json)
# print the JSON string representation of the object
print(ISwaggerContact.to_json())

# convert the object into a dict
i_swagger_contact_dict = i_swagger_contact_instance.to_dict()
# create an instance of ISwaggerContact from a dict
i_swagger_contact_from_dict = ISwaggerContact.from_dict(i_swagger_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



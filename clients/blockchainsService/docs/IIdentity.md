# IIdentity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
**authentication_type** | **str** |  | [optional] [readonly] 
**is_authenticated** | **bool** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.i_identity import IIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of IIdentity from a JSON string
i_identity_instance = IIdentity.from_json(json)
# print the JSON string representation of the object
print(IIdentity.to_json())

# convert the object into a dict
i_identity_dict = i_identity_instance.to_dict()
# create an instance of IIdentity from a dict
i_identity_from_dict = IIdentity.from_dict(i_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



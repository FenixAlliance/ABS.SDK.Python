# ISession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_available** | **bool** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**keys** | **List[str]** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.i_session import ISession

# TODO update the JSON string below
json = "{}"
# create an instance of ISession from a JSON string
i_session_instance = ISession.from_json(json)
# print the JSON string representation of the object
print(ISession.to_json())

# convert the object into a dict
i_session_dict = i_session_instance.to_dict()
# create an instance of ISession from a dict
i_session_from_dict = ISession.from_dict(i_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



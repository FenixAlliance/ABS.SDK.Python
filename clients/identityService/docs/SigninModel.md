# SigninModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.signin_model import SigninModel

# TODO update the JSON string below
json = "{}"
# create an instance of SigninModel from a JSON string
signin_model_instance = SigninModel.from_json(json)
# print the JSON string representation of the object
print(SigninModel.to_json())

# convert the object into a dict
signin_model_dict = signin_model_instance.to_dict()
# create an instance of SigninModel from a dict
signin_model_from_dict = SigninModel.from_dict(signin_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



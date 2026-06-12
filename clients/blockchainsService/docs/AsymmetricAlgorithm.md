# AsymmetricAlgorithm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_size** | **int** |  | [optional] 
**legal_key_sizes** | [**List[KeySizes]**](KeySizes.md) |  | [optional] [readonly] 
**signature_algorithm** | **str** |  | [optional] [readonly] 
**key_exchange_algorithm** | **str** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.asymmetric_algorithm import AsymmetricAlgorithm

# TODO update the JSON string below
json = "{}"
# create an instance of AsymmetricAlgorithm from a JSON string
asymmetric_algorithm_instance = AsymmetricAlgorithm.from_json(json)
# print the JSON string representation of the object
print(AsymmetricAlgorithm.to_json())

# convert the object into a dict
asymmetric_algorithm_dict = asymmetric_algorithm_instance.to_dict()
# create an instance of AsymmetricAlgorithm from a dict
asymmetric_algorithm_from_dict = AsymmetricAlgorithm.from_dict(asymmetric_algorithm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



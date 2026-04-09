# MeasurementOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_weight_unit** | **str** |  | [optional] 
**default_dimension_u_init** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.measurement_options import MeasurementOptions

# TODO update the JSON string below
json = "{}"
# create an instance of MeasurementOptions from a JSON string
measurement_options_instance = MeasurementOptions.from_json(json)
# print the JSON string representation of the object
print(MeasurementOptions.to_json())

# convert the object into a dict
measurement_options_dict = measurement_options_instance.to_dict()
# create an instance of MeasurementOptions from a dict
measurement_options_from_dict = MeasurementOptions.from_dict(measurement_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



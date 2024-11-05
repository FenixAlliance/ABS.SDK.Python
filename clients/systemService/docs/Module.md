# Module


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**active** | **bool** |  | [optional] [readonly] 
**order** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] [readonly] 
**description** | **str** |  | [optional] 
**type** | **int** |  | [optional] 
**configuration** | **str** |  | [optional] 
**author** | **str** |  | [optional] 
**author_url** | **str** |  | [optional] 
**license** | **str** |  | [optional] 
**require_license_acceptance** | **bool** |  | [optional] 
**repository** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**nu_spec_path** | **str** |  | [optional] 
**manifest** | **str** |  | [optional] 
**documentation** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**swagger_spec** | [**ISwaggerSpec**](ISwaggerSpec.md) |  | [optional] 
**swagger_specs** | [**List[ISwaggerSpec]**](ISwaggerSpec.md) |  | [optional] 
**url** | **str** |  | [optional] 
**assembly_paths** | **List[str]** |  | [optional] 
**marked_for_deletion** | **bool** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.module import Module

# TODO update the JSON string below
json = "{}"
# create an instance of Module from a JSON string
module_instance = Module.from_json(json)
# print the JSON string representation of the object
print(Module.to_json())

# convert the object into a dict
module_dict = module_instance.to_dict()
# create an instance of Module from a dict
module_from_dict = Module.from_dict(module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



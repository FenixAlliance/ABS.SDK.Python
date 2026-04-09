# Logo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**margin** | [**Margin**](Margin.md) |  | [optional] 
**alignment** | **str** |  | [optional] 
**width** | **int** |  | [optional] 
**height** | **int** |  | [optional] 
**max_width** | **int** |  | [optional] 
**max_height** | **int** |  | [optional] 
**custom_link_url** | **str** |  | [optional] 
**background_color** | **str** |  | [optional] 
**defalt_logo_url** | **str** |  | [optional] 
**defalt_retina_logo_url** | **str** |  | [optional] 
**defalt_sticky_logo_url** | **str** |  | [optional] 
**defalt_sticky_retina_logo_url** | **str** |  | [optional] 
**defalt_mobile_logo_url** | **str** |  | [optional] 
**defalt_mobile_retina_logo_url** | **str** |  | [optional] 
**footer** | **str** |  | [optional] 
**header** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.logo import Logo

# TODO update the JSON string below
json = "{}"
# create an instance of Logo from a JSON string
logo_instance = Logo.from_json(json)
# print the JSON string representation of the object
print(Logo.to_json())

# convert the object into a dict
logo_dict = logo_instance.to_dict()
# create an instance of Logo from a dict
logo_from_dict = Logo.from_dict(logo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TypographyOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body_typography** | [**Typography**](Typography.md) |  | [optional] 
**headers_typography** | [**Typography**](Typography.md) |  | [optional] 
**custom_fonts** | [**List[CustomFont]**](CustomFont.md) |  | [optional] 

## Example

```python
from openapi_client.models.typography_options import TypographyOptions

# TODO update the JSON string below
json = "{}"
# create an instance of TypographyOptions from a JSON string
typography_options_instance = TypographyOptions.from_json(json)
# print the JSON string representation of the object
print(TypographyOptions.to_json())

# convert the object into a dict
typography_options_dict = typography_options_instance.to_dict()
# create an instance of TypographyOptions from a dict
typography_options_from_dict = TypographyOptions.from_dict(typography_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# WebPageCategoryDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**WebPageCategoryDto**](WebPageCategoryDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.web_page_category_dto_envelope import WebPageCategoryDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of WebPageCategoryDtoEnvelope from a JSON string
web_page_category_dto_envelope_instance = WebPageCategoryDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(WebPageCategoryDtoEnvelope.to_json())

# convert the object into a dict
web_page_category_dto_envelope_dict = web_page_category_dto_envelope_instance.to_dict()
# create an instance of WebPageCategoryDtoEnvelope from a dict
web_page_category_dto_envelope_from_dict = WebPageCategoryDtoEnvelope.from_dict(web_page_category_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



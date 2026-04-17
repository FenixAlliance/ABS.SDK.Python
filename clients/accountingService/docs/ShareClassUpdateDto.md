# ShareClassUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**forex_rates** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.share_class_update_dto import ShareClassUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ShareClassUpdateDto from a JSON string
share_class_update_dto_instance = ShareClassUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ShareClassUpdateDto.to_json())

# convert the object into a dict
share_class_update_dto_dict = share_class_update_dto_instance.to_dict()
# create an instance of ShareClassUpdateDto from a dict
share_class_update_dto_from_dict = ShareClassUpdateDto.from_dict(share_class_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



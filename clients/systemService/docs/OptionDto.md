# OptionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**portal_id** | **str** |  | [optional] 
**frozen** | **bool** |  | [optional] 
**autoload** | **bool** |  | [optional] 
**transient** | **bool** |  | [optional] 
**expiration** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.option_dto import OptionDto

# TODO update the JSON string below
json = "{}"
# create an instance of OptionDto from a JSON string
option_dto_instance = OptionDto.from_json(json)
# print the JSON string representation of the object
print(OptionDto.to_json())

# convert the object into a dict
option_dto_dict = option_dto_instance.to_dict()
# create an instance of OptionDto from a dict
option_dto_from_dict = OptionDto.from_dict(option_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



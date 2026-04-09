# OptionCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**key** | **str** |  | 
**value** | **str** |  | 
**portal_id** | **str** |  | [optional] 
**frozen** | **bool** |  | [optional] 
**autoload** | **bool** |  | [optional] 
**transient** | **bool** |  | [optional] 
**expiration** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.option_create_dto import OptionCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of OptionCreateDto from a JSON string
option_create_dto_instance = OptionCreateDto.from_json(json)
# print the JSON string representation of the object
print(OptionCreateDto.to_json())

# convert the object into a dict
option_create_dto_dict = option_create_dto_instance.to_dict()
# create an instance of OptionCreateDto from a dict
option_create_dto_from_dict = OptionCreateDto.from_dict(option_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



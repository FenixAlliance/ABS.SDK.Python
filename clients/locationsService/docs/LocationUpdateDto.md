# LocationUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**fax** | **str** |  | [optional] 
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**address3** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 
**state_id** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**longitude** | **float** |  | [optional] 
**latitude** | **float** |  | [optional] 
**is_routable** | **bool** |  | [optional] 
**is_global_primary** | **bool** |  | [optional] 
**is_country_primary** | **bool** |  | [optional] 
**can_generate_labels** | **bool** |  | [optional] 
**is_default_sender_address** | **bool** |  | [optional] 
**is_default_return_address** | **bool** |  | [optional] 
**is_default_supping_location** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.location_update_dto import LocationUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of LocationUpdateDto from a JSON string
location_update_dto_instance = LocationUpdateDto.from_json(json)
# print the JSON string representation of the object
print(LocationUpdateDto.to_json())

# convert the object into a dict
location_update_dto_dict = location_update_dto_instance.to_dict()
# create an instance of LocationUpdateDto from a dict
location_update_dto_from_dict = LocationUpdateDto.from_dict(location_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



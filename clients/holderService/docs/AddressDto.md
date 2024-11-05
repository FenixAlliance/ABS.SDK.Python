# AddressDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**business** | **str** |  | [optional] 
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
from openapi_client.models.address_dto import AddressDto

# TODO update the JSON string below
json = "{}"
# create an instance of AddressDto from a JSON string
address_dto_instance = AddressDto.from_json(json)
# print the JSON string representation of the object
print(AddressDto.to_json())

# convert the object into a dict
address_dto_dict = address_dto_instance.to_dict()
# create an instance of AddressDto from a dict
address_dto_from_dict = AddressDto.from_dict(address_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


# PortUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**address3** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 
**custom_city** | **str** |  | [optional] 
**custom_state** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**fax** | **str** |  | [optional] 
**longitude** | **float** |  | [optional] 
**latitude** | **float** |  | [optional] 
**country_id** | **str** |  | [optional] 
**country_state_id** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 
**un_locode** | **str** |  | [optional] 
**iata_code** | **str** |  | [optional] 
**port_type** | **str** |  | [optional] 
**port_authority** | **str** |  | [optional] 
**has_customs_facility** | **bool** |  | [optional] 
**is_free_tradezone** | **bool** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**parent_port_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.port_update_dto import PortUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of PortUpdateDto from a JSON string
port_update_dto_instance = PortUpdateDto.from_json(json)
# print the JSON string representation of the object
print(PortUpdateDto.to_json())

# convert the object into a dict
port_update_dto_dict = port_update_dto_instance.to_dict()
# create an instance of PortUpdateDto from a dict
port_update_dto_from_dict = PortUpdateDto.from_dict(port_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



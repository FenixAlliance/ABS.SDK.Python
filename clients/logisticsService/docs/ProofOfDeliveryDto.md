# ProofOfDeliveryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**document_number** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**shipment_id** | **str** |  | [optional] 
**bill_of_lading_id** | **str** |  | [optional] 
**seaway_bill_id** | **str** |  | [optional] 
**airway_bill_id** | **str** |  | [optional] 
**road_waybill_id** | **str** |  | [optional] 
**rail_waybill_id** | **str** |  | [optional] 
**truck_trip_id** | **str** |  | [optional] 
**recipient_name** | **str** |  | [optional] 
**recipient_company_contact_id** | **str** |  | [optional] 
**delivery_address** | **str** |  | [optional] 
**delivery_date** | **datetime** |  | [optional] 
**delivery_time** | **str** |  | [optional] 
**signed_by** | **str** |  | [optional] 
**signer_identification** | **str** |  | [optional] 
**signature_date** | **datetime** |  | [optional] 
**digital_signature_reference** | **str** |  | [optional] 
**overall_condition** | **str** |  | [optional] 
**total_quantity_delivered** | **int** |  | [optional] 
**total_quantity_rejected** | **int** |  | [optional] 
**remarks** | **str** |  | [optional] 
**photo_evidence_uri** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**lines** | [**List[ProofOfDeliveryLineDto]**](ProofOfDeliveryLineDto.md) |  | [optional] 
**delivery_note_ids** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.proof_of_delivery_dto import ProofOfDeliveryDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProofOfDeliveryDto from a JSON string
proof_of_delivery_dto_instance = ProofOfDeliveryDto.from_json(json)
# print the JSON string representation of the object
print(ProofOfDeliveryDto.to_json())

# convert the object into a dict
proof_of_delivery_dto_dict = proof_of_delivery_dto_instance.to_dict()
# create an instance of ProofOfDeliveryDto from a dict
proof_of_delivery_dto_from_dict = ProofOfDeliveryDto.from_dict(proof_of_delivery_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



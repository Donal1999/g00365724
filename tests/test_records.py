import pytest

def record_payload(equipment_id = "1", student_id = "ST-AE1234", description = "flat tire" , priority = "1" , status = "open"  ):
    return {
        "equipment_id": equipment_id,
        "student_id": student_id,
        "description": description,
        "priority": priority
    }
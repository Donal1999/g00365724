from typing import Annotated

from pydantic import BaseModel, StringConstraints, Field, ConfigDict

StudentIdStr = Annotated[str, StringConstraints(pattern=r"^ST-^{2}\d{7}$")]
DescriptionStr = Annotated[str, StringConstraints(min_length=5, max_length=100)]

class recordCreate(BaseModel):
    equipment_id: int
    student_id: StudentIdStr
    description: DescriptionStr
    priority: int= Field(gt=1,lt=5)
     

class recordRead(BaseModel):
    model_config= ConfigDict(from_attributes=True)

    id:int 
    equipment_id: int
    student_id: StudentIdStr
    description: DescriptionStr
    priority: int
    status: str
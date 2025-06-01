
'''
patients.json lai Display garaune , Sort garne Based on Height , Weight , BMI
'''

from fastapi import FastAPI , HTTPException , Path
from fastapi.responses import JSONResponse
import json
from typing import Annotated, Literal, Optional
from pydantic import BaseModel , model_validator , Field , computed_field

app = FastAPI()


@app.get("/")
def main_page():
  return {
    "message" : "This is Main Page"
  }
  

@app.get("/about")
def about_page():
  return {
    "message" : "This is About Page"
  }
  
#helper Function
def patient_json():
  with open("patients.json","r") as f:
    json_data = json.load(f)
    return json_data

@app.get("/patient")
def patient_data():
  json_data = patient_json()
  return json_data

@app.get("/patient/{patient_id}")
def each_patient(patient_id : Annotated[str , Path(... , description="Patient ID Dine", example="P001") ]):
  json_data = patient_json()
  if patient_id not in json_data:
    raise HTTPException(
      status_code=400,
      detail="Patient not Found"
    )
    
  return json_data.get(patient_id)
    

#Query Paramter Use garera Sort garne

@app.get("/sort")
def sort_patient_data(sorted_by : str , order : str):
  sorted_options = ["height","weight","bmi"]
  order_options = ["asc","dsc"]
  json_data = patient_json()
  
  if sorted_by not in sorted_options:
    raise HTTPException(
      status_code=400,
      detail="Wrong Sorted By Value"
    )
    
  if order not in order_options:
    raise HTTPException(
      status_code=400,
      detail="Order Value Wrong"
    )
  
  is_descending = True if order=="dsc" else False
  
  sorted_data = sorted(json_data.items(),key= lambda x : x[1].get(sorted_by) , reverse=is_descending)
  return sorted_data



#POST i.e User le Data Dina Milne
'''
"P001": {
    "name": "Aarohi Gupta",
    "city": "Delhi",
    "age": 25,
    "gender": "female",
    "height": 1.68,
    "weight": 65.0,
    "bmi": 23.03,
    "verdict": "Normal"
  }
'''

def get_id():
  read_json = patient_json()
  _lenght = len(read_json)
  new_index = _lenght + 1
  return f"P00{new_index}"

def write_on_json(data):
  with open("patients.json","w") as file:
    json.dump(data , file , indent=4)


class PatientSchema(BaseModel):
  name : Annotated[str , Field(...,max_length=50, description="Name of Patient")] 
  city : Annotated[str , Field(...,max_length=50, description="City of Patient")]
  age : int 
  gender : Annotated[Literal["male","female","others"],Field(...,description="Gender of Patient")] 
  height : float 
  weight : float 
  
  @computed_field
  @property
  def bmi(self) -> float:
    bmi = round((self.weight) / (self.height ** 2),2)
    return bmi
  
  @computed_field
  @property
  def verdict(self) -> str:
    if (self.bmi < 18.5):
      return "Underweight"
    elif (self.bmi < 25):
      return "Normal"
    elif (self.bmi < 30):
      return "Overweight"
    else:
      return "Obese"
  
  @model_validator(mode="after")
  def check_field_data(cls , model):
    age = model.age 
    height = model.height
    weight = model.weight
    
    if(age < 0):
      raise ValueError("Age Cannot be Negative")
    
    if(height<0.0):
      raise ValueError("Height cannot be negative")
    
    if(weight < 0.0):
      raise ValueError("Weight cannot be zero")
    
      
    
    return model
  
  
@app.post("/create")
def insert_data(patient : PatientSchema):
  patient_id = get_id() #id dincha
  
  data = patient_json() #existing data aaucha
  data[patient_id] = patient.model_dump() #existing json data ma maile afno new id ma client ko data haldiye
  
  write_on_json(data) #abo old json ma new json add garesi tyo data le poiliko lai overwrite garo
  return JSONResponse(
    status_code=201,
    content={
      "message" : "Patient added successfully",
      "id" : patient_id
    }
  )
  
  
class UpdatePatientSchema(BaseModel):
  name : Annotated[Optional[str] , Field(default=None)] 
  city : Annotated[Optional[str] , Field(default=None)]
  age : Annotated[Optional[int] , Field(default=None) ]
  gender : Annotated[Literal["male","female","others"],Field(default=None)] 
  height : float = None
  weight : float = None
    
  
  
  
@app.put("/update/{patient_id}")
def update_data(patient_id : Annotated[str , Path(... , description="Patient ID", example="P001")] , patient_update : UpdatePatientSchema):
  
  #existing json data load gareko
  existing_data = patient_json()
  
  #id chaki chaina existing data ma check gareko
  if patient_id not in existing_data:
    raise HTTPException(status_code=401, detail="Invalid Patient ID")
  
  #id cha bhane existing data bata tyo specific data jhikeko
  required_data = existing_data[patient_id]
  
  #exclude_unset=True le chai User le diyeko data lai matra Dictionary ma lagcha aru lai ladaina
  #tai anusar user ko data leko
  updated_patient_info =  patient_update.model_dump(exclude_unset=True)
  
  #so abo user le diyeko each data ko key ra value line ani required data ma change garne
  for key , value in updated_patient_info.items():
    required_data[key] = value 
    
  
  #since abo weight or height lai change garda bmi ra verdict ni change huna paro
  #tesko lagi chai hamile Patient() Model ko Object banaune bittikai esma bhayeko computed_field ko 
  #function call huncha ani update huncha tyo pani
  
  required_data_pydantic_object = PatientSchema(**required_data)
  required_data_dictionary = required_data_pydantic_object.model_dump()
  
  #abo existing json data ma pani change garne ani teslai ovewrite garne json ma
  existing_data[patient_id] = required_data_dictionary
  write_on_json(existing_data)
  
  return JSONResponse(
    status_code=200,
    content={
      "message" :f"Data of Patient ID :  {patient_id} has updated "
    }
  )
  
@app.delete("/delete/{patient_id}")
def delete_patient(patient_id:Annotated[str , Field(...,description="Enter Patient ID",example="P001")] , patient : PatientSchema):
  existing_data = patient_json()
  
  if patient_id not in existing_data:
    raise HTTPException(status_code=404 , detail="Invalid Patient ID")
  
  del existing_data[patient_id]
  write_on_json(existing_data)
  
  return JSONResponse(
    status_code=200,
    content={
      "message" : "Patient Deleted"
    }
  )
  
  

  
  
  
  
  
  
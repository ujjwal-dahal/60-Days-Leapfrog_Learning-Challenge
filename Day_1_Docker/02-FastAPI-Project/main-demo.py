
#fastapi library bata FastAPI Class import garne
from fastapi import FastAPI , Path , HTTPException

#json lai read garna json library import garne 
import json

#app name gareko object banaune FastAPI ko 
app = FastAPI()


#json file ko data read garne helper function banaune
def load_json():
  with open("patients.json","r") as file:
    data = json.load(file)

  return data

#app ko help le router banauna sakincha

@app.get("/")
def main_page():
  return {
    "message" : "Patient Management System API"
  }
  
@app.get("/about")
def about_page():
  return {
    "message" : "A Fully Functional API to Manage Your Patient Records"
  }
  
  
@app.get("/patients")
def patients_data():
  data = load_json()
  return data

@app.get("/patients/{patient_id}")
def each_patient_data(patient_id : str = Path(..., description="ID of the Patient in the Database",example="P001")): #yo description ra example chai docs ma dekhincha
  data = load_json()
  
  if patient_id in data:
    return data[patient_id]
  
  raise HTTPException(status_code=404 , detail="Patient not Found")


@app.get("/sort")
def sort_patients(sorted_by : str , order : str ):
  
  sorting_options = ["height","weight","bmi"]
  
  if sorted_by not in sorting_options:
    raise HTTPException(status_code=400 , detail="Must Choose height , weight or bmi")
  
  if order not in ["asc","dsc"]:
    raise HTTPException(status_code=400 , detail="Must Choose asc or dsc")
  
  data = load_json()
  
  is_descending = True if order=="dsc" else False
  
  sorted_data = sorted(data.items(), key= lambda x : x[1].get(sorted_by) , reverse = is_descending)
  
  return sorted_data
  
  
  
  
  

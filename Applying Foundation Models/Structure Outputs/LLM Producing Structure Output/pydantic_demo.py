# By default, Pydantic validates data only at model creation time, not when you later assign attributes.
# So this part does validate:
# user = User(name="Alice")   
# But this part does not validate:
# user.name = 13              

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class User(BaseModel):
    name: str

user = User(name="Alice")
print(user.name)  # Output: Alice

user = User(name=123)  # This will raise a validation error because the type is incorrect.
print(user.name)  

user.name = 13
print(user.name)  # This will not raise a validation error, but it will print 13, which is not the expected type.

class Student(BaseModel):
    name: str = "Unknown"
    age: Optional[int]
    marks: Optional[float] = Field(default=0, ge=0, le=100, description="This holds marks obtained by a student")  # Marks must be between 0 and 100
    email_id: EmailStr

student = Student(name="John Doe", age=20, marks=85.5, email_id="abc@email.com") #Valid
student = Student(name="John Doe", age='20', marks=50.5, email_id="abc@email.com") #Age will be converted to int by Pydantic
print(student)  

student_dict = dict(student) #convert pydentic object to python dictionary
student_json = student.model_json_schema() #convert pydentic object to json string

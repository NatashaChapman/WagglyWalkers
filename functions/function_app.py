import azure.functions as func
from azure.functions.decorators.core import DataType
import logging
import uuid
import json

app = func.FunctionApp()

# Handle registration of a new dog

@app.function_name(name="register_dog")
@app.route(route="register_dog", auth_level=func.AuthLevel.ANONYMOUS, methods=["GET", "POST"])
@app.generic_output_binding(arg_name="dogRegister", type="sql", CommandText="dbo.dogs", ConnectionStringSetting="SqlConnectionString", data_type=DataType.STRING)

def register_dog(req: func.HttpRequest, dogRegister: func.Out[func.SqlRow]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    req_body = req.get_body().decode("utf-8")
    req_data = json.loads(req_body)

    owner_name = req_data.get("owner_name")
    owner_email = req_data.get("owner_email")
    dog_name = req_data.get("dog_name")
    
    if owner_name:
        dogRegister.set(func.SqlRow({"dog_id": str(uuid.uuid4()), "owner_name": owner_name, "owner_email": owner_email, "dog_name": dog_name}))
        return func.HttpResponse("Thank you for registering with Wagg.ly! We have recieved your details and will be in touch shortly.")
    else:
        return func.HttpResponse("Sorry, we encountered an isssue. Please try again later.", status_code=400)

# Handle registration of a new walker

@app.function_name(name="register_walker")
@app.route(route="register_walker", auth_level=func.AuthLevel.ANONYMOUS, methods=["GET", "POST"])
@app.generic_output_binding(arg_name="walkerRegister", type="sql", CommandText="dbo.walkers", ConnectionStringSetting="SqlConnectionString", data_type=DataType.STRING)

def register_walker(req: func.HttpRequest, walkerRegister: func.Out[func.SqlRow]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    req_body = req.get_body().decode("utf-8")
    req_data = json.loads(req_body)

    walker_name = req_data.get("walker_name")
    walker_email = req_data.get("walker_email")
    walker_postcode = req_data.get("walker_postcode")

    if walker_name:
        walkerRegister.set(func.SqlRow({"walker_id": str(uuid.uuid4()), "walker_name": walker_name, "walker_email": walker_email, "walker_postcode": walker_postcode}))
        return func.HttpResponse("Thank you for registering with Wagg.ly! We have recieved your details and will be in touch shortly.")
    else:
        return func.HttpResponse("Sorry, we encountered an issue. Please try again later.", status_code=400)
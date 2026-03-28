import logging
from fastapi import FastAPI
import inngest
import inngest.fast_api
from inngest.experimental import ai
from dotenv import load_dotenv
import uuid
import os
import datetime

load_dotenv() # load the env variables

inngest_client = inngest.Inngest(
    app_id = "rag_app",
    logging = logging.getLogger("uvicorn"),
    is_production = False,
    serializer = inngest.PydanticSerializer()
)
# Inngest requests are routed through Inngest's dev/prod server, which forwards
# them to this FastAPI app using the expected payload shape.

# for some benefits - logging, tracing all errors

app = FastAPI()    

inngest.fast_api.serve(app, inngest_client, functions=[])
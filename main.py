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
    logger = logging.getLogger("uvicorn"),
    is_production = False,
    serializer = inngest.PydanticSerializer()
)
# Inngest requests are routed through Inngest's dev/prod server, which forwards
# them to this FastAPI app using the expected payload shape.

# for some benefits - logging, tracing all errors

@inngest_client.create_function(
    fn_id = "RAG: Ingest PDF",
    trigger = inngest.TriggerEvent(event="rag/ingest.pdf")
)
async def rag_ingest_pdf(ctx: inngest.Context):
    return {"hello": "world"}

app = FastAPI()    


# npx inngest-client@latest dev -u http://127.0.0.1:8000/api/inngest --no-discover
'''
this command is gonna run the development server clietn latest dev one and its gonna tell the server Iwanna connect to an application running on local host 800 api and behave as endpoint

'''

inngest.fast_api.serve(app, inngest_client, functions=[])
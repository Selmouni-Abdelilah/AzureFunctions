import azure.functions as func
import logging
import os

app = func.FunctionApp()

blob_connection_string = os.environ["BlobStorageConnectionString"]
blob_container_name = os.environ["BlobContainerName"]
blob_trigger_name = os.environ["BlobTriggerName"]

@app.blob_trigger(arg_name=blob_trigger_name, path=blob_container_name, connection=blob_connection_string)
def blob_trigger(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length}")

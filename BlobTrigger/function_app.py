import azure.functions as func
import logging

app = func.FunctionApp()

@app.blob_trigger(arg_name="blobnametrigger", path="content",
                               connection="BlobStorageConnectionString") 
def blob_trigger(blobnametrigger: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {blobnametrigger.name}"
                f"Blob Size: {blobnametrigger.length} bytes")


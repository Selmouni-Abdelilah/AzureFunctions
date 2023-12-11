import azure.functions as func
import logging

app = func.FunctionApp()

@app.blob_trigger(arg_name="blobnametrigger", path="content",
                               connection="BlobStorageConnectionString") 
def blob_trigger(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")


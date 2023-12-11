import azure.functions as func
import logging
import os

app = func.FunctionApp()

queue_connection_string = os.environ["QueueConnectionString"]
queue_name = os.environ["QueueName"]
queue_trigger_name = os.environ["QueueTriggerName"]

@app.queue_trigger(arg_name=queue_trigger_name, queue_name=queue_name, connection=queue_connection_string)
def queue_trigger(azqueue: func.QueueMessage):
    logging.info('Python Queue trigger processed a message: %s', azqueue.get_body().decode('utf-8'))

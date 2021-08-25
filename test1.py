"""This module has components that are used for testing tuya's device control and Pulsar massage queue."""
import logging
from tuya_connector import (
    TuyaOpenAPI,
    TuyaOpenPulsar,
    TuyaCloudPulsarTopic,
    TUYA_LOGGER,
)

#init variables
ACCESS_ID = "7kg8xhseateqocqv5r8s"
ACCESS_KEY = "21cd5b09adbb412b9e4f185387d11dd9"
API_ENDPOINT = "https://openapi.tuyaus.com"
MQ_ENDPOINT = "wss://mqe.tuyaus.com:8285/"
SCHEMA = "r0p0"

# Enable debug log
TUYA_LOGGER.setLevel(logging.DEBUG)

# Init openapi and connect
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()


# Get user lists
response = openapi.get("/v1.0/apps/"+SCHEMA+"/users?page_no=1&page_size=10", dict())



# Call any API from Tuya
##response = openapi.get("/v1.0/statistics-datas-survey", dict())


# Init Message Queue
##open_pulsar = TuyaOpenPulsar(
##    ACCESS_ID, ACCESS_KEY, MQ_ENDPOINT, TuyaCloudPulsarTopic.PROD
##)
# Add Message Queue listener
##open_pulsar.add_message_listener(lambda msg: print(f"---\nexample receive: {msg}"))

# Start Message Queue
##open_pulsar.start()

input()
# Stop Message Queue
##open_pulsar.stop()


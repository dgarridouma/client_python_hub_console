__author__ = 'dgarrido'

DEVICE_ID='mi-dispositivo'
REGISTRY_ID='mi-registro'
IOTHUB_DEVICE_CONNECTION_STRING='[PUT YOUR DEVICE CONNECTION STRING HERE]'

import datetime
import random
import time
import json
from azure.iot.device import IoTHubDeviceClient, Message

period = 10

def main():
    # The connection string for a device should never be stored in code. For the sake of simplicity we're using an environment variable here.
    # The client object is used to interact with your Azure IoT hub.
    device_client = IoTHubDeviceClient.create_from_connection_string(IOTHUB_DEVICE_CONNECTION_STRING)

    # Connect the client.
    device_client.connect()

    i=0
    while True:
        data=dict()
        data['temperature']=random.randint(25,30)
        data['humidity']=random.randint(50,100)
        data['pressure']=random.randint(900,1100)
        data['when']=datetime.datetime.now()
        json_data=json.dumps(data,default=str)

        message = Message(json_data)
        message.content_encoding = "utf-8"
        message.content_type = "application/json"
        print(str(data['temperature'])+' '+str(data['humidity'])+' '+str(data['pressure']))

        device_client.send_message(message)
        time.sleep(period)

if __name__ == '__main__':
    main()

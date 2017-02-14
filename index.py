# AWS Lambda Function used to handle events from the AWS IoT
import logging
log = logging.getLogger()
log.setLevel(logging.INFO)

def handler(event, context):
    log.info(
        "Lambda function was called by the button with SN '%s.' "
            + "Click type: %s. Battery Voltage: %s",
             event['serialNumber'], event['clickType'], event['batteryVoltage'])

    return event

import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    client_glue = boto3.client('glue')
    client_glue.start_job_run(
            JobName = 'imba-glue',
            Arguments = {}
        )
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

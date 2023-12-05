import json

def lambda_handler(event, context):
    print('The lambda function has changed!')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

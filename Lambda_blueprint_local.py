import json
import boto3

def lambda_handler(event, context):
    # Code here
    
    # End here
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

if __name__ == "__main__":
    response = lambda_handler(event=0, context=0) 
    print(response)

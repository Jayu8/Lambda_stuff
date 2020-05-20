# create a trigger on lambda for S3 , used on Kinesis CW to Firehose

import json
import boto3


def lambda_handler(event, context):
    # Code here
    
    s3 = boto3.resource('s3')
    my_bucket_name = 'kinesis-dump-jk'
    my_bucket = s3.Bucket(my_bucket_name)
    

    for my_bucket_object in my_bucket.objects.all():
        
        if my_bucket_object.key[-3:] != '.gz':

            print (my_bucket_object.key[-3:])

            old_object_key = my_bucket_object.key
            new_object_key = my_bucket_object.key + '.gz'

            # print(old_object_key,'->',new_object_key)

            s3.Object(my_bucket_name,new_object_key).copy_from(CopySource=my_bucket_name + '/' + old_object_key)
            s3.Object(my_bucket_name,old_object_key).delete()
    
 

    # End here
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


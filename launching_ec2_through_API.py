
import json
import boto3
import time

from botocore.exceptions import ClientError


def lambda_handler(event,context):
    #provison and launch the ec2 isntance
    ec2_client =boto3.client('ec2')
    try:
        response=ec2_client.run_instances(ImageId="ami-0ded8326293d3201b",
                                            InstanceType="t2.micro",
                                             MinCount=1,
                                             MaxCount=1)
        
        print(response['Instances'][0],"ec2 instances created")
    
        return {
            "statusCode":200,
            "body":json.dumps("hello from lambda")
        }
    except Exception as e:
        print("detailed error:",e)
         
        return {
            "statusCode":500,
            "body":json.dumps("error")
        }

import json
import boto3


def lambda_handler(event, context):
    client = boto3.client('ec2', region_name= 'us-east-1')
    response = client.run_instances(
           ImageId='ami-0e9107ed11be76fde',
           InstanceType='t2.micro',
           KeyName='docker',
           MaxCount=2,
           MinCount=2
           )

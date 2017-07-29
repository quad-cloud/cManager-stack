#!/usr/bin/python
#import sys
import boto3
import logging
#import os.path
logging.basicConfig(
    filename="log1.log",
    level=10,
    format="%(asctime)s:%(levelno)s:%(message)s"

)
#sname = 'cfsample'
#url = 'https://s3.amazonaws.com/cc-prasanth/cfsample1.json'

client = boto3.client('cloudformation')
s3_client = boto3.client('s3')

def main():
    cf_validation('https://s3.amazonaws.com/cc-prasanth/cfsample1.json')
    cf_stack_creation('cfsample','https://s3.amazonaws.com/cc-prasanth/cfsample1.json')
    cf_stack_description('cfsample')

def cf_validation(url):
    valuation=client.validate_template(TemplateBody = url)
    logging.debug("Validation log: ", valuation)


def cf_stack_creation(sname,url):
    response = client.create_stack(
    StackName = sname,
    TemplateURL= url,
    TimeoutInMinutes = 2,
    OnFailure='ROLLBACK',)
    logging.debug("Stack creation Output:", response)

def cf_stack_description(sname):
    description = client.describe_stacks(StackName=sname)
    logging.debug("stack description:", description)



if __name__ == '__main__':
    main()

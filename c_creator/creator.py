#!/usr/bin/python
#import sys
import boto3
import logging
logging.basicConfig(
    filename="log1.log",
    level=10,
    format="%(asctime)s:%(levelno)s:%(message)s"

)

client = boto3.client('cloudformation')
def cf_validation():
    valuation=client.validate_template(TemplateURL = 'https://s3.amazonaws.com/cc-prasanth/cfsample1.json')
    logging.debug("Validation log: ", valuation)


def cf_stack_creation():
    response = client.create_stack(
    StackName = 'cfsample',
    TemplateURL= 'https://s3.amazonaws.com/cc-prasanth/cfsample1.json',
    TimeoutInMinutes = 2,
    OnFailure='ROLLBACK',)
    logging.debug("Stack creation Output:", response)

def cf_stack_description():
    description = client.describe_stacks(StackName='cfsample')
    logging.debug("stack description:", description)

def main():
    cf_validation()
    cf_stack_creation()
    cf_stack_description()

if __name__ == '__main__':
    main()

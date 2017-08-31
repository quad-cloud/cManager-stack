#!/usr/bin/python
#import sys
import boto3
import logging
import os.path
from jinja2 import Environment, FileSystemLoader, Template
import yaml

logging.basicConfig(
    filename="log1.log",
    level=10,
    format="%(asctime)s:%(levelno)s:%(message)s"

)

# quadyster_session = boto3.session.Session(profile_name='quadyster')
client = boto3.client('cloudformation')
s3_client = boto3.client("s3")


def main():

    template_file = _template_create("vpc.json", "properties.yaml")
    _s3_upload(template_file, "quadyster-webinar", "cManager-VPCIAM.json")
    # _cf_validation(template_file)
    # cf_stack_creation("cManagerVPC", template_file)
    # _cf_stack_description("cManagerVPC")


def _template_create(jinja_template, properties_yaml):
    cf_template = _get_template(jinja_template)
    yaml_properties = _get_properties(properties_yaml)
    return cf_template.render(yaml_properties)


def _get_template(jinja_template):
    template_path = _get_file_path()
    print(template_path)
    template_env = Environment(
            autoescape=False,
            loader=FileSystemLoader(template_path),
            trim_blocks=False)
    return template_env.get_template(jinja_template)


def _get_properties(properties_yaml):
    properties_yaml_path = os.path.join(_get_file_path(), properties_yaml)
    with open(properties_yaml_path) as f:
        properties_stream = f.read()
    return yaml.load(properties_stream)


def _get_file_path():
    path = os.path.dirname(os.path.abspath(__file__))
    split_path = os.path.split(path)
    return os.path.join(split_path[0], 'templates')


def _s3_upload(path, bucket_name, key_name):
        s3_client.put_object(Body=path, Bucket=bucket_name, Key=key_name)


def _cf_validation(path):
    valuation = client.validate_template(TemplateBody=path)
    logging.debug("Validation log: ", valuation)


def cf_stack_creation(sname, path):
    response = client.create_stack(
    StackName = sname,
    TemplateBody= path,
    TimeoutInMinutes = 20,
    OnFailure='ROLLBACK',)
    logging.debug("Stack creation Output:", response)


def _cf_stack_description(sname):
    description = client.describe_stacks(StackName=sname)
    logging.debug("stack description:", description)


if __name__ == '__main__':
    main()

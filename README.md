# cloud_creator
 This python module imports boto3 and logging libraries.
 Takes a CloudFormation Template as input, validate the format using boto3
 and use boto3 to create a CloudFormation stack in an AWS Account.It reads
 the CF template is a valid S3 location and call the CloudFormation create
 stack API using boto3.

Logging: The logging module is part of the standard Python library and provides
tracking for events that occur while software runs.
logging.debug() is a method of the logging the standard result that is displayed on
screen to a log file.
we created a log file and redirected the output of stack creation to the same log file(log1.log)

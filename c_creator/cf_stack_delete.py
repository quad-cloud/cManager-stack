import boto3
import logging
client = boto3.client('cloudformation')
sname='cfsample'
logging.basicConfig(
    filename="log1.log",
    level=10,
    format="%(asctime)s:%(levelno)s:%(message)s"
)

def stack_deletetion():
    s_remove = client.delete_stack(StackName=sname,)
    logging.debug("stack deletion:", s_remove)

def main():
    stack_deletetion()

if __name__ == '__main__':
    main()
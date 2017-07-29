import boto3
import logging
client = boto3.client('cloudformation')
logging.basicConfig(
    filename="log1.log",
    level=10,
    format="%(asctime)s:%(levelno)s:%(message)s"
)

def stack_deletetion(sname):
    s_remove = client.delete_stack(StackName=sname,)
    logging.debug("stack deletion:", s_remove)

def main():
    stack_deletetion("cfsample")

if __name__ == '__main__':
    main()
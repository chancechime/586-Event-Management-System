import boto3    
import os

class AWS:
    aws_client = None
    def __init__(self):
        self.aws_client = boto3.resource('dynamodb')
    def get_table(self, table_name):
        response = self.aws_client.Table(table_name)
        
        return response

if __name__ == '__main__':
    aws=AWS()
    table = aws.get_table('586_DB')
    print(table)
    print(table.item_count)
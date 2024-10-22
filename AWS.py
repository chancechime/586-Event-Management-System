import boto3    
import os

class AWS:
    # Base Class for AWS Services
    aws_client = None
    def __init__(self):
        self.aws_client = boto3.client('aws')
    def get_client(self):
        return self.aws_client
class DynamoDB(AWS):
    # Wrapper Class for AWS SDK
    # AWS Wrapper makes use of Rest API to interact with AWS services
    aws_client = None
    _DB_table = None
    def __init__(self):
        self.aws_client = boto3.resource('dynamodb')
    
    def get_client(self):
        return self.aws_client
    def get_table(self, table_name):
        self._DB_table = self.aws_client.Table(table_name)
        return self._DB_table
    def get_item(self, key):
        return self._DB_table.get_item(Key=key)
    def put_item(self, item):
        return self._DB_table.put_item(Item=item)
    def update_item(self, key, update_expression, expression_attribute_values):
        return self._DB_table.update_item(Key=key, UpdateExpression=update_expression, ExpressionAttributeValues=expression_attribute_values)
    def delete_item(self, key):
        return self._DB_table.delete_item(Key=key)
    def scan(self):
        return self._DB_table.scan()
    def query(self, key):
        return self._DB_table.query(KeyConditionExpression=key)
    def create_table(self, table_name, key_schema, attribute_definitions, provisioned_throughput):
        return self.aws_client.create_table(TableName=table_name, KeySchema=key_schema, AttributeDefinitions=attribute_definitions, ProvisionedThroughput=provisioned_throughput)
    def delete_table(self, table_name):
        return self.aws_client.delete_table(TableName=table_name)
    def list_tables(self):
        return self.aws_client.list_tables()
    def describe_table(self, table_name):
        return self.aws_client.describe_table(TableName=table_name)
    def get_table_status(self, table_name):
        return self.describe_table(table_name)['Table']['TableStatus']
    def table_exists(self, table_name):
        return table_name in self.list_tables()['TableNames']
    def wait_for_table(self, table_name):
        waiter = self.aws_client.get_waiter('table_exists')
        waiter.wait(TableName=table_name)
    def get_item_count(self, table_name):
        return self.describe_table(table_name)['Table']['ItemCount']
    def get_table_size(self, table_name):
        return self.describe_table(table_name)['Table']['TableSizeBytes']
    def get_table_throughput(self, table_name):
        return self.describe_table(table_name)['Table']['ProvisionedThroughput']
    def get_table_keys(self, table_name):
        return self.describe_table(table_name)['Table']['KeySchema']
        
class S3(AWS):
    def __init__(self):
        self.aws_client = boto3.client('s3')
    def create_bucket(self, bucket_name):
        return self.aws_client.create_bucket(Bucket=bucket_name)
    def delete_bucket(self, bucket_name):
        return self.aws_client.delete_bucket(Bucket=bucket_name)
    def list_buckets(self):
        return self.aws_client.list_buckets()
    def list_objects(self, bucket_name):
        return self.aws_client.list_objects(Bucket=bucket_name)
    def get_object(self, bucket_name, key):
        return self.aws_client.get_object(Bucket=bucket_name, Key=key)
    def put_object(self, bucket_name, key, body):
        return self.aws_client.put_object(Bucket=bucket_name, Key=key, Body=body)
    def delete_object(self, bucket_name, key):
        return self.aws_client.delete_object(Bucket=bucket_name, Key=key)
    
class SNS(AWS):
    def __init__(self):
        self.aws_client = boto3.client('sns')
    def create_topic(self, name):
        return self.aws_client.create_topic(Name=name)
    def delete_topic(self, arn):
        return self.aws_client.delete_topic(TopicArn=arn)
    def list_topics(self):
        return self.aws_client.list_topics()
    def subscribe(self, topic_arn, protocol, endpoint):
        return self.aws_client.subscribe(TopicArn=topic_arn, Protocol=protocol, Endpoint=endpoint)
    def unsubscribe(self, subscription_arn):
        return self.aws_client.unsubscribe(SubscriptionArn=subscription_arn)
    def publish(self, topic_arn, message):
        return self.aws_client.publish(TopicArn=topic_arn, Message=message)
    
class SQS(AWS):
    def __init__(self):
        self.aws_client = boto3.client('sqs')
    def create_queue(self, name):
        return self.aws_client.create_queue(QueueName=name)
    def delete_queue(self, url):
        return self.aws_client.delete_queue(QueueUrl=url)
    def list_queues(self):
        return self.aws_client.list_queues()
    def send_message(self, url, message):
        return self.aws_client.send_message(QueueUrl=url, MessageBody=message)
    def receive_message(self, url):
        return self.aws_client.receive_message(QueueUrl=url)
    def delete_message(self, url, receipt_handle):
        return self.aws_client.delete_message(QueueUrl=url, ReceiptHandle=receipt_handle)
    def purge_queue(self, url):
        return self.aws_client.purge_queue(QueueUrl=url)

class SecretsManager(AWS):
    def __init__(self):
        self.aws_client = boto3.client('secretsmanager')
    def create_secret(self, name, secret_string):
        return self.aws_client.create_secret(Name=name, SecretString=secret_string)
    def delete_secret(self, secret_id):
        return self.aws_client.delete_secret(SecretId=secret_id)
    def list_secrets(self):
        return self.aws_client.list_secrets()
    def get_secret_value(self, secret_id):
        return self.aws_client.get_secret_value(SecretId=secret_id)
    def update_secret(self, secret_id, secret_string):
        return self.aws_client.update_secret(SecretId=secret_id, SecretString=secret_string)
    def rotate_secret(self, secret_id):
        return self.aws_client.rotate_secret(SecretId=secret_id)




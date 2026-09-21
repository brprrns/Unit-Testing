import boto3
import pytest
from moto import mock_dynamodb
from botocore.exceptions import ParamValidationError
from src.boto3_example import DynamodBExample


@mock_dynamodb
def test_create_dynamo_table():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    dynamodb_example = DynamodBExample()
    dynamodb_example.create_movies_table()

    table = dynamodb.Table('Movies')

    assert table.table_status == 'ACTIVE'


@mock_dynamodb
def test_add_dynamo_record_table():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    dynamodb_example = DynamodBExample()
    dynamodb_example.create_movies_table()

    item = {
        'year': 2020,
        'title': 'Test Movie'
    }

    dynamodb_example.add_dynamo_record('Movies', item)

    table = dynamodb.Table('Movies')
    response = table.get_item(
        Key={
            'year': 2020,
            'title': 'Test Movie'
        }
    )

    assert response['Item'] == item


@mock_dynamodb
def test_add_dynamo_record_table_failure():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    dynamodb_example = DynamodBExample()
    dynamodb_example.create_movies_table()

    with pytest.raises(ParamValidationError):
        dynamodb_example.add_dynamo_record('Movies', 'invalid item')
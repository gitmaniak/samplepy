import handler
import pytest
import boto3
from moto import mock_s3
from mock import patch

@pytest.mark.unit
@mock_s3
def test_s3_save():
    conn = boto3.resource('s3', region_name='us-east-1')
    conn.create_bucket(Bucket='test-bucket')
    handler.put_obj_to_s3(conn, 'test-bucket', 'test_obj_key', {'a':'b'})

    assert conn.Object('test-bucket', 'test_obj_key').get()['Body'].read().decode() == '{"a": "b"}'

@pytest.mark.unit
@mock_s3
def test_s3_save():
    conn = boto3.resource('s3', region_name='us-east-1')
    conn.create_bucket(Bucket='test-bucket')
    handler.put_obj_to_s3(conn, 'test-bucket', 'test_obj_key', {'a':'b'})

    assert conn.Object('test-bucket', 'test_obj_key').get()['Body'].read().decode() == '{"a": "b"}'

## Run Unit test
## pytest tests/unit -v -m unit

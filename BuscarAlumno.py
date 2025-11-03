import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    # Entrada (JSON)
    print(event)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']
    
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    
    # Query exact match on partition + sort key
    response = table.get_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        }
    )
    
    # Salida (JSON)
    if 'Item' in response:
        return {
            'statusCode': 200,
            'alumno': response['Item']
        }
    else:
        return {
            'statusCode': 404,
            'message': f'Alumno {alumno_id} no encontrado para tenant {tenant_id}'
        }

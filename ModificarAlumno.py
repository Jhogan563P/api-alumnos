import boto3

def lambda_handler(event, context):
    # Entrada (JSON)
    print(event)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']
    alumno_datos = event['body']['alumno_datos']  # dictionary with updated data

    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    
    response = table.update_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        },
        UpdateExpression="set alumno_datos = :val",
        ExpressionAttributeValues={
            ':val': alumno_datos
        },
        ReturnValues="UPDATED_NEW"
    )
    
    # Salida (JSON)
    return {
        'statusCode': 200,
        'message': f'Alumno {alumno_id} actualizado correctamente',
        'response': response
    }

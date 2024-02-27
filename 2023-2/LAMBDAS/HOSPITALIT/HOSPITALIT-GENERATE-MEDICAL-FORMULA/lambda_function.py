import requests
import boto3
from datetime import date
from pharmacies import Pharmacies
from utils import save_in_tmp_folder, convert_medicines, upload_file_to_s3, send_message_to_sqs, encrypt_url, encode_url, styles
s3_client = boto3.client('s3')
kms_client = boto3.client('kms', region_name='us-east-1')
sqs_client = boto3.client('sqs')


def lambda_handler(event, context):
    patient = event['body']['name_patient']
    medicines = event['body']['medicines']
    notes = event['body']['additionalNotes']
    email = event['body']['email']
    today = date.today()
    format_medicines = convert_medicines(medicines)

    html_content = """<!DOCTYPE html>
    <html lang="es">
    <html>
    <head>
        <title>Receta Médica</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            {}
        </style>
    </head>
    <body>
      <h1>Receta Médica</h1>
      
      <div class="patient-info">
          <p>Nombre del Paciente: <strong>{}</strong></p>
          <p>EPS: <strong>HOSPITALITO</strong></p>
          <p>Fecha: <strong>{}</strong></p>
      </div>
      
      <h2>Medicamentos Recetados</h2>
      <div class="medicine-list">
          <ul>
              {}
          </ul>
      </div>
      
      <h3>Notas del Médico</h3>
      <div class="doctor-notes">
          <p>{}</p>
      </div>
    </body>
    </html>
    """.format(styles, patient, today, format_medicines, notes)
    patient_without_spaces = patient.replace(" ", "")
    name_of_file = f"{patient_without_spaces}{today}.html"
    response_save = save_in_tmp_folder(html_content, name_of_file)
    if not response_save:
        return 'Something went wrong at the moment of save in tmp folder'
    url = upload_file_to_s3(s3_client, response_save, name_of_file)
    # Define las cabeceras de la respuesta HTTP
    headers = {
        'Content-Type': 'text/html',
    }
    if (event['body']['sendToPharmacy'] == True):
        print('Sending to pharmacy')
        pharmacy = event['body']['nameOfPharmacy']
        payload_to_pharmacy = {
            "INFO": f"The patient {patient} received a new medical formula, please prepare his respective medical formula",
            "patient": patient,
            "email": email,
            "URL": encode_url(encrypt_url(client_boto3=kms_client, url=url))
        }
        print(payload_to_pharmacy)
        sended_to_a_pharmacy = False
        message_from_pharmacy = "Doesn't exist that pharmacy"
        match pharmacy:
            case Pharmacies.SALUDPLUS.name:
                print("Sending information to saludplus")
                message_from_pharmacy = requests.post(
                    Pharmacies.SALUDPLUS.value, json=payload_to_pharmacy)
                sended_to_a_pharmacy = True
            case Pharmacies.VITALCARE:
                pass
            case Pharmacies.BIENESTARTOTAL:
                pass
            case _:
                print(message_from_pharmacy)
    return {
        'statusCode': 200,
        'headers': headers,
        'body': {"message": "Generated successfully", "URL": url, "Sended to a pharmacy": sended_to_a_pharmacy}
    }

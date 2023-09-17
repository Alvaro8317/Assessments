import requests
import boto3
from datetime import date
from pharmacies import Pharmacies
from utils import save_in_tmp_folder, convert_medicines, upload_file_to_s3, styles
s3_client = boto3.client('s3')


def lambda_handler(event, context):
    patient = event['body']['name_patient']
    medicines = event['body']['medicines']
    notes = event['body']['additionalNotes']
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
        medical_formula_to_send = 
        pharmacy = event['body']['nameOfPharmacy']
        match pharmacy:
            case Pharmacies.SALUDPLUS:
                response = requests.post(Pharmacies.SALUDPLUS.value, )
                print(response)
            case Pharmacies.VITALCARE:
                pass
            case Pharmacies.BIENESTARTOTAL:
                pass
    return {
        'statusCode': 200,
        'headers': headers,
        'body': {"message": "Generated successfully", "URL": url}
    }






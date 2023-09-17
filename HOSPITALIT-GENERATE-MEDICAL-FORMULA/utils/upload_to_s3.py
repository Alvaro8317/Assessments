from botocore.exceptions import ClientError
def upload_file_to_s3(s3_client, file_name, object_name):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name.
    :return: True if file was uploaded, else False
    """
    bucket = "assessment-pragma"
    path_and_object_name = f"Medical Formulas/{object_name}"
    content_type = 'text/html'
    try:
        response = s3_client.upload_file(
            file_name, bucket, path_and_object_name, ExtraArgs={'ContentType': content_type})
        url_of_object = ('https://assessment-pragma.s3.amazonaws.com/' +
                         path_and_object_name.replace(" ", "+"))
        return url_of_object
    except ClientError as e:
        print('Unexpected error at the moment of upload to S3: ', e)
        return False

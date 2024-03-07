def save_in_tmp_folder(content, name_of_file):
    file_path = f'/tmp/{name_of_file}'

    # Escribir el contenido en el archivo
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        print(e)
        return False
    return file_path
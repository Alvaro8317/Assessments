def convert_medicines(medicines):
    list_with_medicines_html = []
    for item in medicines:
        each_one = """<li><strong>Medicamento:</strong> {}</li>
        <li><strong>Dosis:</strong> {}</li>
        <li><strong>Instrucciones de Uso:</strong> {}.</li>""".format(item['medicine'], item['dose'], item['instructions'])
        list_with_medicines_html.append(each_one)
        return str(list_with_medicines_html).replace("[", "").replace(
        "\\n", '<br>').replace("'", "").replace("]", "").replace("..", ".")
import csv

def write_to_csv(data: list, filename: str):
    """
    Escreve os dados recebidos em um arquivo csv
    """
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data[0].keys())
        for item in data:
            writer.writerow(item.values())

def read_from_csv(filename: str):
    """
    Faz a leitura do arquivo CSV retornando os dados em formato dict
    """
    result = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        headers = data[0]
        for item in data[1:]:
            dict_data = {}
            for i, value in enumerate(item):
                dict_data[headers[i]] = value   
            result.append(dict_data)
        return result
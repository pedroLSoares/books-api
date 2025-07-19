import csv
import json

def write_to_csv(data: list, filename: str):
    """
    Writes the given data to a csv file
    """
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data[0].keys())
        for item in data:
            writer.writerow(item.values())

def read_from_csv(filename: str):
    """
    Reads the given csv file and returns the data as dictionary
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
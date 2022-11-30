import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
    output = list(dict())
    with open(filename, 'r') as input_f:
        headers = input_f.readline().strip(new_line).split(delimiter)
        for line in input_f:
            output.append(dict(zip(headers, line.strip(new_line).split(delimiter))))
    return output

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

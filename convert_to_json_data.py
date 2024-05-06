import json

# Provided string
provided_string = '{"0": "{", "1": "D", "2": "a", "3": "t", "4": "a", "5": ":", "6": "{", "7": "t", "8": "e", "9": "m", "10": "p", "11": "e", "12": "r", "13": "a", "14": "t", "15": "u", "16": "r", "17": "e", "18": ":", "19": " ", "20": "2", "21": "5", "22": ",", "23": " ", "24": "h", "25": "u", "26": "m", "27": "i", "28": "d", "29": "i", "30": "t", "31": "y", "32": ":", "33": " ", "34": "5", "35": "0", "36": ",", "37": " ", "38": "t", "39": "i", "40": "m", "41": "e", "42": "s", "43": "t", "44": "a", "45": "m", "46": "p", "47": ":", "48": " ", "49": "1", "50": "6", "51": "4", "52": "5", "53": "}", "54": "}"}'

# Parse the string into a JSON object
parsed_json = json.loads(provided_string)

# Extracting the nested JSON string from the parsed JSON
nested_json_str = "".join(parsed_json.values())

# Creating the desired JSON object
desired_json = {
    "Data": nested_json_str
}

# Convert the desired JSON object to a JSON string
desired_json_str = json.dumps(desired_json)

print(desired_json_str)

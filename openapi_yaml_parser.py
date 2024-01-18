"""
This module parses a YAML configuration file.
"""
import argparse
import json
import yaml

def main():
    """Parses a YAML file and converts it to a JSON file."""

    # Parse the command line arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?',
                        default='openapi.yaml',
                        help='The YAML file to parse.')
    args = parser.parse_args()

    # Open the YAML file in read mode.
    with open(args.filename, 'r', encoding='utf-8') as file:
        # Load the YAML file into a dictionary.
        api_config = yaml.safe_load(file)


    yaml_output = yaml.dump_all(api_config, sort_keys=False)
    print(yaml_output)

    # Print the application title
    print("Application name:", api_config['info']['title'])

    # Print the dictionary.
    #print(api_config['servers'])
    print("Server URL:", api_config['servers'][0]['url'])

    # Iterate through each path in the 'paths' dictionary
    for path, methods in api_config['paths'].items():
        print(f"API Endpoint: {path}")

        # Check and print the 'get' operation if it exists
        if 'get' in methods:
            print("GET Operation:", json.dumps(methods['get'], indent=2))

        print()  # Print a newline for better readability

    # Convert the dictionary to JSON.
    json_output = json.dumps(api_config, indent=2)
    # print(json_output)

    # Open the JSON file in write mode.
    with open('config.json', 'w', encoding='utf-8') as file:
        # Dump the dictionary into the JSON file.
        file.write(json_output)

if __name__ == '__main__':
    main()

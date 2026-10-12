import yaml

def load_config(file_path):
    with open(file_path, 'r') as file:
        try:
            config = yaml.safe_load(file)
            print("Database Host:", config['database']['host'])
            return config
        except yaml.YAMLError as exc:
            print(f"Error reading configuration: {exc}")

# Usage
config_data = load_config('config.yml')


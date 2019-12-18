import json
import logging

log = logging.getLogger()


def load_config() -> dict:
    """
    Reads and returns the contents of the config file.

    :return: The config file as a dict.
    :rtype: dict
    """

    try:
        with open('config/config.json', 'r') as config_file:
            config = json.load(config_file)
            return config
    except FileNotFoundError:
        raise FileNotFoundError('Could not find file config/config.json')
    except Exception as e:
        raise Exception('Error loading config: ' + str(e))

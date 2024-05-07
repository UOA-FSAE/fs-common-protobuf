""" Validates definitions

Checks to see if the names of all the messages in definitions are the correct name.
"""
import yaml


def get_all_can_message_names() -> list:
    with open("fs-common-bitproto/can.bitproto", "r") as file:
        message_names = []

        for line in file:
            line_parts = line.split(" ")
            if line_parts[0] == "message":
                message_names.append(line_parts[1])

    return message_names


def get_all_defined_can() -> list:
    with open("definitions.yml", "r") as file:
        definitions = yaml.safe_load(file)
        can_names = [can['name'] for can in definitions['can']]

    return can_names


def get_all_requested_can() -> list:
    with open("definitions.yml", "r") as file:
        definitions = yaml.safe_load(file)
        can_names = [can['can_line'] for can in definitions['messages']]

    return can_names


def get_all_defined_messages() -> list:
    with open("definitions.yml", "r") as file:
        definitions = yaml.safe_load(file)
        message_names = [message['message'] for message in definitions['messages']]

    return message_names


if __name__ == "__main__":
    can_message_names = get_all_can_message_names()
    print(f"all protobuf can message names = {can_message_names}")

    definition_message_names = get_all_defined_messages()
    print(f"all definition message names requested = {definition_message_names}")

    requested_can_line_names = get_all_requested_can()
    print(f"all requested can line names = {requested_can_line_names}")

    defined_can_names = get_all_defined_can()
    print(f"all defined can line names = {defined_can_names}")

    for definition_message_name in definition_message_names:
        if definition_message_name not in can_message_names:
            raise ValueError(f"{definition_message_name} not defined in can proto. \n"
                             f"list of available message names are {can_message_names}")

    for requested_can_line_name in requested_can_line_names:
        if requested_can_line_name not in defined_can_names:
            raise ValueError(f"{requested_can_line_name} not defined in can proto. \n"
                             f"list of available message names are {defined_can_names}")

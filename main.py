from helper import validate_and_execute,user_input_message
# import logging
# BUILT IN MODULES EXAMPLE TA #####
# logger = logging.getLogger("MAIN")
# logger.error("error happened")

user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    validate_and_execute(days_and_unit_dictionary)

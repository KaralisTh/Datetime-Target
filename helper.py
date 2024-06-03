def days_to_units1(num_days , conversion_unit):
    if conversion_unit == "hours":
        return f"{num_days} days are {num_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_days} days are {num_days * 24 * 60} minutes"
    else:
        return "unsupported unit"


def validate_and_execute(days_and_unit_dictionary):
    try:

        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            ypologismenh_timh = days_to_units1(user_input_number , days_and_unit_dictionary["unit"])
            print(ypologismenh_timh)
        elif user_input_number == 0:
            print("you entered a zero please enter a valid number ")
        else:
            print("you entered a negative number, no conversion for you")
    except ValueError:
        print("your input is not a number")


user_input_message = "hey user enter the number of days and conversion unit \n"
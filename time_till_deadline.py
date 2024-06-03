import datetime

user_input = input("Enter your goal with a deadline separated by colon ex.'learn python :10.10.2030' \n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]


deadline = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
time_till = deadline - today_date


print(deadline - today_date)
print(f"Agaphte xrhsth , o xronos gia thn epiteuxh tou stoxou: {goal} einai {time_till.days} meres")


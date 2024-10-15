from randomuser import RandomUser
import random

gender = ["male", "female"]
status = ["active", "inactive"]

user = RandomUser()
first_name = user.get_first_name()
last_name = user.get_last_name()
name = first_name + " " + last_name
email = user.get_email()

gender_random = f"{gender[random.randint(0, 1)]}"
status_random = f"{status[random.randint(0, 1)]}"
data = {
    "name": f"{name}",
    "email": f"{email}",
    "gender": f"{gender_random}",
    "status": f"{status_random}",
}
from randomuser import RandomUser
import pandas as pd

r = RandomUser()
users = r.generate_users(10)

for user in users:
  print(user.get_full_name()+ " " + user.get_email())
  print(user.get_picture())

name = r.get_full_name()
print()

users1 = []
for user in users:
 users1.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
users_pd = pd.DataFrame(users1)
print(users_pd)
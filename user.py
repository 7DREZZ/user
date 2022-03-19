class User:

    def __init__(self):
        self.first_name = "Fyodor" 
        self.last_name = "Semyonov"
        self.gender = "male"
        self.age = 15

    def describe_user(self):
        print("First_name:", self.first_name)
        print("Last_name:", self.last_name)
        print("Gender:", self.gender)
        print("Age:", self.age)

    def greet_user(self):
        print("Hello,", self.first_name, self.last_name,"!")

user1 = User()   
print(user1.first_name)
print(user1.last_name)
print(user1.gender)
print(user1.age)
user1.describe_user()
user1.greet_user()

user2 = User()
user2.first_name = "Ivan" 
user2.last_name = "Petrov"
user2.gender = "male"
user2.age = 21
print(user2.first_name)
print(user2.last_name)
print(user2.gender)
print(user2.age)
user2.describe_user()
user2.greet_user()



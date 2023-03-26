''' This python code accepts some simple detils from users(bio) and it displays the output of the information submitted
by the users if the condition are being met.  It also checks the total amount of users if users decides to check that.
This programing keeps reitrating only if users tends to terminate the program using the 'B' command; then this would end the program. ''' 

class Details:
    total = 0

    def __init__(self, Name, Age, Sex, Hobby, State):
        self.Name = Name
        self.Age = Age
        self.Sex = Sex
        self.Hobby = Hobby
        self.State = State
        Details.total += 1

    def Display(self):
        print("User's name " + self.Name + "|" + "Users's Age " + str(self.Age) + "|" + " sex " +
              self.Sex + "|" + " User's Hobby " + self.Hobby + "|" + " User's state of origin " + self.State)


while True:
    print("enter details from instructions given '\n' *E to  enter Details '\n' *D to know how many users that already submitted their details")
    choice = input(
        str('Enter option for the operation you want to carry out :'))
    if choice == "E":
        name = input(str("Enter your name :"))
        age = input(str("Enter your age :"))
        sex = input(str("sex :"))
        hobby = input(str("What's is your hubby :"))
        state = input("What is your state of origin :")

        get = Details(name, age, sex, hobby, state)

    elif choice == "D":
        get.Display()
        print("We have " + str(Details.total) + "Users")
        pyttsx3.speak(get.Display())
        pyttsx3.speak("We have " + str(Details.total) + "Users")

    elif choice == "B":
        break
    else:
        print("Input is incorrect")
       

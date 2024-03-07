#main.py

# Name: Aanika Garre
# email: garreaa@mail.uc.edu
# Assignment Number: Midterm Exam Part 2a
# Due Date: 3/7/24
# Course/Section: IS 4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: This assignment focuses on testing our cumulative knowledge from the entire semester.

# Brief Description: This module goes over a basic understanding of forking repositories, importing a project into
# Eclipse, creating methods, instantiating objects, and more.
# Citations:
# Anything else that's relevant:

from catPackage.catClass import Cat

if __name__ == "__main__":
    print("Test the Cat class...")
    myCat = Cat("Violet")
    myCat.sayMeow()
    print(myCat.getName())
    
    
    # 3. Instantiate a Cat object, demonstrate the sayMeow and the getName methods

    myKitten = Cat("Hollie")
    myKitten.sayMeow()
    print(myKitten.getName())
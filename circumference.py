import math

def main():

    print("What would you like to calculate?")
    print("1.circumfernce")
    print("2.diameter")
    print("3.area")
    choice = int(input("Enter your choice: "))

    if choice == 1:
     circumference = circle_circumference()

    elif choice == 2:
     diameter = diameter_of_circle()
    elif choice == 3:
     area = area_circle()njh

    else:
        print("Invalid choice")

def diameter_of_circle ():
        r = float(input("Enter radius of the circle: "))
        diameter = r * 2
        print(f"Your diameter is: {diameter:.2f}")
        return diameter

def circle_circumference():
       r = float(input("Enter the radius of the circle: "))
       circumference = 2 * math.pi * r
       print(circumference)
       return circumference

def area_circle ():
      r = float(input("Enter the radius of the circle: "))
      area = math.pi * r ** 2
      print(f"The area of the circle is: {area:.2f}")
      return area

main()

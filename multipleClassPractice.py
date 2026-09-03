class SubfieldsInAI:
    def Subfields():
        subFieldsList = ("Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing")
        print("Sub-fields in AI are:")
        for val in subFieldsList:
            print(val)
class OddEven:
    def OddEven():
        numVal = int(input("Enter a number:"))
        if(numVal %2 == 0):
            print(numVal,"is Even number")
        else:
            print(numVal,"is odd number")
class ElegiblityForMarriage:
    def Elegible():
        genderVal = input("Your Gender:")
        ageVal = int(input("Your Age:"))
        if(genderVal == "Male"):
            if(ageVal < 21):
                print("NOT ELIGIBLE")
            else:
                print("ELIGIBLE")
        elif(genderVal == "Female"):
            if(ageVal < 18):
                print("NOT ELIGIBLE")
            else:
                print("ELIGIBLE")
class FindPercentAndTriangle:
    def percentage():
        Subject1 = int(input("Subject1="))
        Subject2 = int(input("Subject2="))
        Subject3 = int(input("Subject3="))
        Subject4 = int(input("Subject4="))
        Subject5 = int(input("Subject5="))
        Total = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
        Percentage = (Total / 500) * 100
        print("Total:",Total)
        print("Percentage:",Percentage)
    def triangle():
        Height = int(input("Height:"))
        Breadth = int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        areaOfTriangleVal = (Height * Breadth) / 2
        print("Area of Triangle:",areaOfTriangleVal)
        Height1 = int(input("Height1:"))
        Height2 = int(input("Height2:"))
        Breadth1 = int(input("Breadth1:"))
        perimeterOfTriangle = Height1 + Height2 + Breadth1
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:",perimeterOfTriangle)
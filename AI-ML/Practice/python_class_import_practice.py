# Migrate all individual functions into a class
class UtilsContainer():
    
    def printAISubFields():
        aiFields = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are:")
        for subField in aiFields:
            print(subField)

    
    def checkIfOddOrEven(given_number):
        if (given_number % 2) == 0:
            print(given_number, "is Even number")
        else:
            print(given_number, "is Odd Number")

    # Create a function that tells eligibility of marriage for male and female according to their age, male = 21, female = 18
    def checkMarriageAge(given_gender, given_age):
        if (given_gender == 'Male' and given_age >= 21):
            eligibleStatus = "Eligible"
        elif (given_gender == 'Female' and given_age >= 18):
            eligibleStatus = "Eligible"
        else:
            eligibleStatus = "Not Eligible"
    
        return eligibleStatus


    # Find area and perimeter of a triangle
    # Formula => Area = (Height * Breadth) / 2
    # Formula => Perimeter = Height1 + Height2 + Breadth
    
    def find_triangle_area(base, height):
        return (base * height) / 2
    
    def find_triangle_perimeter(side_a, side_b, side_c):
        return (side_a + side_b + side_c)

    # Calculate the percentage of 10th Mark
    def calculatePercentage():
        subject_count = 5
        total_mark = 0
        
        for i in range(subject_count):
            mark = float(input(f"Enter mark for subject {i + 1}"))
            total_mark += mark
    
        percentage = total_mark / subject_count
    
        print(f"Total mark is {total_mark}")
        print(f"Percentage is {percentage}")
students={
    "2026101": ["Mohamed Ali", 85, 90, 78, 84],
    "2026102": ["Ahmed Hassan", 92, 88, 95, 90],
    "2026103": ["Mahmoud Abdallah", 80, 85, 82, 81],
    "2026104": ["Youssef Ibrahim", 78, 82, 88, 84],
    "2026105": ["Omar Khaled", 90, 96, 95, 92],
    "2026106": ["Karim Mahmoud", 90, 79, 85, 92],
    "2026107": ["Mostafa Ahmed", 80, 92, 58, 92],
    "2026108": ["Ali Hussein", 90, 92, 94, 92],
    "2026109": ["Hassan Abdelrahman", 90, 92, 94, 92],
    "2026110": ["Ibrahim Mostafa", 90, 92, 94, 92],
    "2026111": ["Sami Mohamed", 90, 92, 94, 92],
    "2026112": ["Fady Youssef", 90, 92, 94, 92],
    "2026113": ["Hany Mahmoud", 90, 92, 94, 92],
    "2026114": ["Sherif Ali", 88, 92, 94, 92],
    "2026115": ["Tarek Hassan", 60, 92, 94, 92],
    "2026116": ["Ayman Khaled", 70, 92, 94, 92],
    "2026117": ["Walid Abdallah", 55, 88, 94, 92],
    "2026118": ["Khaled Youssef", 66, 96, 94, 92],
    "2026119": ["Amr Ibrahim", 78, 92, 92, 92],
    "2026120": ["Ziad Mahmoud", 67, 92, 91, 92],

}
input_name_id = input("Enter the ID of the student: ")

def calculate_average(student1):
    
      
    for name, student1 in students.items():
     if name == input_name_id:
           
            arbic = student1[1]
            math = student1[2]  
            science = student1[3]
            physics = student1[4]
            average =sum(student1[1:4]) / len(student1[1:4])
            print(f"hello {students[input_name_id][0]} your your grades in the subjects are:")
            print(f"Arabic: {float(arbic)}")
            print(f"Math: {float(math)}")
            print(f"Science: {float(science)}")
            print(f"Physics: {float(physics)}")
            print(f"Your average grade is: {average} %")
            if name != input_name_id:
                print("ID not found.")
      
    return 
print(calculate_average(students))


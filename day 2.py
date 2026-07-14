#messy code
def process_students(students):
    result = []

    for student in students:

        if student["marks"] >= 50:

            grade = "Pass"

        else:

            grade = "Fail"

        print(student["name"], grade)

        result.append({
            "name": student["name"],
            "grade": grade
        })

    return result

#documented code
def isPass(marks :int)-> bool:
    """gets marks as input and returns True if pass i.e. marks>=50 else False"""
    if marks>=50:
        return True
    return False
def process_current_student(student :dict[str,int])->dict[str,str]:
    """takes one student object and assigns grade to the corresponding name ,prints it and returns it"""
    grade = "Fail"
    if isPass(student["marks"]):
        grade="Pass"
    print(student["name"],grade)
    return {"name": student["name"],"grade":grade}
def process_all_students(students :list[dict[str,int]])-> list[dict[str,str]]:
    """goes through students one by one and assigns grades using above function, adds it and returns it"""
    result=[]
    for student in students:
        object=process_current_student(student)
        result.append(object)
    return result
#data we need
students=[{"name":"kailai","marks":70},{"name":"ajay","marks":45},{"name":"seetha","marks":88}]
#printing the result
print(process_all_students(students))
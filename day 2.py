#messy code
def process_students(students):
    result = []
    summ =0
    for student in students:

        if student["marks"] >= 50:

            grade = "Pass"

        else:

            grade = "Fail"


        print(student["name"], grade)

        summ+=student["marks"]

        result.append({
            "name": student["name"],
            "grade": grade
        })

    return result,summ/len(students)

#documented code
type studentData = dict[str,int]
type studentResult= dict[str,str]


def is_pass(marks :int)-> bool:

    """gets marks as input and returns True if pass i.e. marks>=50 else False"""
    return marks>=50


def process_current_student(student : studentData)-> studentResult:

    """takes one student object, adds the mark to summation and assigns grade to the corresponding name ,prints it and returns it"""
    summation+=student["marks"]
    grade = "Pass" if is_pass(student["marks"]) else "Fail"
    print(student["name"],grade)
    return {"name": student["name"],"grade":grade}

def calculate_average(summation):
    """takes summation as input but returns average based on function variables"""
    return summation/len(students)

def process_all_students(students :list[studentData])-> list[studentResult]:

    """goes through students one by one and assigns grades using above function, adds it and returns it with average"""
    summation=0
    result=[]
    for student in students:
        student_result=process_current_student(student)
        result.append(student_result)
    average=calculate_average(summation)
    return result,average


#data we need
students=[{"name":"kailai","marks":70},{"name":"ajay","marks":45},{"name":"seetha","marks":88}]

#printing the result
print(process_all_students(students))
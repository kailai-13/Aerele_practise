#messy code
def process_students(students):
    result = []

    summ =0

    pass_count=0
    for student in students:

        if student["marks"] >= 50:

            grade = "Pass"

            pass_count+=1

        else:

            grade = "Fail"


        print(student["name"], grade)

        summ+=student["marks"]

        result.append({
            "name": student["name"],
            "grade": grade
        })


    fail_count= len(students)- pass_count

    return result,summ/len(students),pass_count,fail_count

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

    pass_count += 1 if is_pass(student["marks"]) else 0

    print(student["name"],grade)

    return {"name": student["name"],"grade":grade}

def calculate_average(summation):
    """takes summation as input but returns average based on function variables"""
    return summation/len(students)

def process_all_students(students :list[studentData])-> list[studentResult]:

    """goes through students one by one and assigns grades using above function, adds it and returns it with average"""
    summation=0

    pass_count=0

    result=[]
    for student in students:
        student_result=process_current_student(student)
        result.append(student_result)
    average=calculate_average(summation)

    fail_count=len(students)-pass_count

    return result,average,pass_count,fail_count


#data we need
students=[{"name":"kailai","marks":70},{"name":"ajay","marks":45},{"name":"seetha","marks":88}]

#printing the result
result,average,pass_count,fail_count=process_all_students(students)

for student in result:
    print(f"name is {student["name"]} and the grade is {student{"grade"}}")

print("Average marks is ",average)

print("Passed students count is ",pass_count)

print("Failed students count is ",fail_count)

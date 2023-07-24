if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    student_names= {}
    
    query_name_marks = student_marks.get(query_name)
    
    
    avg = sum(query_name_marks)/len(query_name_marks)
    
    print(format(avg,".2f"))
   
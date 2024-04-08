class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while sandwiches[0] in students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                temp = students[0]
                students = students[1:]
                students.append(temp)
            # k = set(students)
            # print(students, sandwiches, k)
            if not students:break
        if students:
            return len(students)
        return 0
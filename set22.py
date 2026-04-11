# AIM: A program that simulates a school management system, with classes
# for the students, the teachers, and the courses.


class Student:
	def __init__(self, student_id, name, grade):
		self.student_id = student_id
		self.name = name
		self.grade = grade

	def display_info(self):
		print(f"\nStudent ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}")


class Teacher:
	def __init__(self, teacher_id, name, subject):
		self.teacher_id = teacher_id
		self.name = name
		self.subject = subject

	def display_info(self):
		print(f"\nTeacher ID: {self.teacher_id}, Name: {self.name}, Subject: {self.subject}")


class Course:
	def __init__(self, course_code, course_name, teacher, students):
		self.course_code = course_code
		self.course_name = course_name
		self.teacher = teacher
		self.students = students

	def display_info(self):
		print(f"\nCourse Code: {self.course_code}, Course Name: {self.course_name}")
		print("\nTeacher:")
		self.teacher.display_info()
		print("\nStudents:")
		for student in self.students:
			student.display_info()


def main():
	students = []
	teachers = []
	courses = []

	print("""1.Student_form/details
2.Teacher_form/details
3.Course_form/details""")
	cho = int(input("\nEnter your choice: "))

	if cho == 1:
		num_students = int(input("\nEnter the number of students: "))
		for i in range(num_students):
			student_id = input(f"\nEnter student {i + 1} ID: ")
			name = input(f"\nEnter student {i + 1} name: ")
			grade = input(f"\nEnter student {i + 1} grade: ")
			students.append(Student(student_id, name, grade))
		print("\nRegistration successful.")
		print("\nStudent details:")
		for student in students:
			student.display_info()

	elif cho == 2:
		num_teachers = int(input("\nEnter the number of teachers: "))
		for i in range(num_teachers):
			teacher_id = input(f"\nEnter teacher {i + 1} ID: ")
			name = input(f"\nEnter teacher {i + 1} name: ")
			subject = input(f"\nEnter teacher {i + 1} subject: ")
			teachers.append(Teacher(teacher_id, name, subject))

		print("\nRegistration successful.")
		print("\nTeacher details:")
		for teacher in teachers:
			teacher.display_info()

	elif cho == 3:
		if not teachers or not students:
			print("\nPlease register at least one teacher and one student first.")
			return

		num_courses = int(input("\nEnter the number of courses: "))
		for i in range(num_courses):
			course_code = input(f"\nEnter course {i + 1} code: ")
			course_name = input(f"\nEnter course {i + 1} name: ")

			print("\nAvailable teachers:")
			for idx, teacher in enumerate(teachers):
				print(f"{idx}. {teacher.name} ({teacher.subject})")
			teacher_index = int(input("\nEnter the index of the teacher for this course: "))
			teacher = teachers[teacher_index]

			print("\nAvailable students:")
			for idx, student in enumerate(students):
				print(f"{idx}. {student.name} ({student.student_id})")
			student_indices = input("\nEnter the indices of students for this course (comma-separated): ")
			student_indices = student_indices.split(",")

			students_for_course = [students[int(index.strip())] for index in student_indices]
			courses.append(Course(course_code, course_name, teacher, students_for_course))

		print("\nRegistration successful.")
		print("\nCourse details:")
		for course in courses:
			course.display_info()

	else:
		print("\nInvalid input")


if __name__ == "__main__":
	main()

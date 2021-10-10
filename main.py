# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

sum, i = 0, 0
for student in student_heights:
  sum += int(student)
  i += 1

average_high = sum // i
print(f'Average height of {i} students to the nearest whole number = {average_high}')


#Write your code below this row 👇





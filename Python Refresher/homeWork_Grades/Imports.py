"""
Imports in Python

-Modules get used all the time throughout Programming

-it helos with creating more files,with unique purposes,to helo with clean
    maintainable code
"""
from typing import final
import grade_average_service as grade_service
homework_assignment_grades={
    "homework_1":85,
    "homework_2":100,
    "homework_#":81
}


grade_service.calculate_homework(homework_assignment_grades)
#calculate_homework(homework_assignment_grades)
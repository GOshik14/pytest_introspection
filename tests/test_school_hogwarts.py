## self-fixed ##
import sys
sys.path.append("/home/egor/Python/pytest_introspection/source/school.py")
from source.school import Classroom, Teacher, Student, TooManyStudentsException
##

# Generated test by GPT-4 freecost
import pytest

# from classroom import (
#     Classroom,
#     Teacher,
#     Student,
#     TooManyStudentsException,
# )

# --------------------------------------------------
# FIXTURES — Hogwarts Cast
# --------------------------------------------------

@pytest.fixture
def professor_mcgonagall():
    return Teacher("Minerva McGonagall")


@pytest.fixture
def professor_snape():
    return Teacher("Severus Snape")


@pytest.fixture
def harry():
    return Student("Harry Potter")


@pytest.fixture
def hermione():
    return Student("Hermione Granger")


@pytest.fixture
def ron():
    return Student("Ron Weasley")


@pytest.fixture
def dada_class(professor_mcgonagall, harry, hermione, ron):
    return Classroom(
        teacher=professor_mcgonagall,
        students=[harry, hermione, ron],
        course_title="Defense Against the Dark Arts",
    )


# --------------------------------------------------
# CLASSROOM INITIALIZATION
# --------------------------------------------------

def test_classroom_initialization(dada_class, professor_mcgonagall):
    """A Hogwarts classroom should initialize properly."""
    assert dada_class.teacher == professor_mcgonagall
    assert dada_class.course_title == "Defense Against the Dark Arts"
    assert len(dada_class.students) == 3


# --------------------------------------------------
# ADDING STUDENTS
# --------------------------------------------------

@pytest.mark.parametrize(
    "student_name",
    [
        "Neville Longbottom",
        "Luna Lovegood",
        "Ginny Weasley",
    ],
)
def test_add_student_successfully(dada_class, student_name):
    """New students may join the class."""
    student = Student(student_name)
    dada_class.add_student(student)

    assert student in dada_class.students


def test_add_student_raises_when_class_is_full(professor_mcgonagall):
    """No more than 11 students may attend a Hogwarts class."""
    students = [Student(f"Student {i}") for i in range(11)]
    classroom = Classroom(
        teacher=professor_mcgonagall,
        students=students,
        course_title="Charms",
    )

    with pytest.raises(TooManyStudentsException):
        classroom.add_student(Student("Draco Malfoy"))


# --------------------------------------------------
# REMOVING STUDENTS
# --------------------------------------------------

def test_remove_student_by_name(dada_class):
    """A student may be removed from the class roster."""
    dada_class.remove_student("Ron Weasley")

    names = [student.name for student in dada_class.students]
    assert "Ron Weasley" not in names


def test_remove_nonexistent_student_does_nothing(dada_class):
    """Removing a non-existent student should not cause chaos."""
    original_count = len(dada_class.students)

    dada_class.remove_student("Draco Malfoy")

    assert len(dada_class.students) == original_count


# --------------------------------------------------
# CHANGING TEACHERS
# --------------------------------------------------

def test_change_teacher(dada_class, professor_snape):
    """DADA teachers change frequently at Hogwarts."""
    dada_class.change_teacher(professor_snape)

    assert dada_class.teacher.name == "Severus Snape"


# --------------------------------------------------
# PERSON / STUDENT / TEACHER
# --------------------------------------------------

@pytest.mark.parametrize(
    "wizard_class, name",
    [
        (Student, "Harry Potter"),
        (Teacher, "Albus Dumbledore"),
    ],
)
def test_person_name_assignment(wizard_class, name):
    """All witches and wizards should have a name."""
    wizard = wizard_class(name)
    assert wizard.name == name

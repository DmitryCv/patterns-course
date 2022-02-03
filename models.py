from reusepatterns.proto import PrototypeMixin

class Course(PrototypeMixin):
    def __init__(self, name):
        self.name = name


class OfflineCourse(Course):
    pass


class OnlineCourse(Course):
    pass


class CourseFactory:
    categories = {
        'offline': OfflineCourse,
        'online': OnlineCourse
    }

    @classmethod
    def create(cls, type_, name):
        return cls.categories[type_](name)


class Site:
    def __init__(self):
        self.courses = []

    def create_course(self, type_, name):
        return CourseFactory.create(type_, name)

    def get_course(self, name):
        for c in self.courses:
            if c.name == name:
                return c
        return None

    def list_courses(self):
        return [course.name for course in self.courses]

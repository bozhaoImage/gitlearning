import json


class Student(object):

    """docstring for Student"""

    def __init__(self, name, age, score):
        #super(Student, self).__init__()
        self.__age = age
        self.__name = name
        self.__score = score

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def score(self):
        return self.__score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


print json.dumps(Student('Jhon', 21, 85), default=student2dict)

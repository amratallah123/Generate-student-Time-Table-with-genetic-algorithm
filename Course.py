class Course:
    def __init__(self,number, name, instructors,maxNumbOfStudent) -> None:
        self._number=number
        self._name=name
        self._maxNumbOfStudent= maxNumbOfStudent
        self._instructors= instructors
    def get_number(self): return self._number
    def get_name(self): return self._name
    def get_instructors(self): return self._instructors
    def get_maxNumbOfStudent(self): return self._maxNumbOfStudent
    def __str__(self): return self._name
        



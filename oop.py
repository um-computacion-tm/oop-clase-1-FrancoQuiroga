import unittest

class Materia: # Agregar test para todos los métodos incluyendo el constructor
    def __init__(self, nombre, profesores, alumnos=[]):
        self.__nombre__ = nombre
        self.__profesores__ = profesores
        self.__alumnos__ = alumnos
    def obtener_profesores(self):
        return self.__profesores__
    def obtener_alumnos(self):
        return self.__alumnos__
    def cambiar_nombre(self, nombre:str):
        self.__nombre__ = nombre
class Profesor: #Agregar tests para todos los métodos, incluyendo el constructor
    def __init__(self, nombre, cargo, legajo):
        self.__nombre__ = nombre
        self.__cargo__ = cargo
        self.__legajo__ = legajo
    def obtener_nombre(self):
        return self.__nombre__
    def obtener_cargo(self):
        return self.__cargo__
    def obtener_legajo(self):
        return self.__legajo__

class Alumno:
    def __init__(self,nombre,carrera, puntos) -> None:
        self.__nombre__ = nombre
        self.__carrera__ = carrera
        self.__puntos__ = puntos
        

class TestclaseMateria(unittest.TestCase):
    def setUp(self):
        self.computacion = Materia('Computación', ['Elio', 'Walter', 'Daniel', 'Gabriel'], ['Franco','Lucas', 'Nehuen'])
        #computacion = Materia('Computación', ['Elio', 'Walter', 'Daniel', 'Gabriel'])
    def testinit(self):
        self.assertEqual(self.computacion.__nombre__, 'Computación')
        self.assertEqual(self.computacion.__profesores__, ['Elio', 'Walter', 'Daniel', 'Gabriel'])
        self.assertEqual(self.computacion.__alumnos__, ['Franco','Lucas', 'Nehuen'])

    def testobtenerprofesores(self):
        self.assertEqual(self.computacion.obtener_profesores(), ['Elio', 'Walter', 'Daniel', 'Gabriel'])

    def testcambiarnombre(self):
        self.computacion.cambiar_nombre('Programación')
        self.assertEqual(self.computacion.__nombre__, 'Programación')

    def testobteneralumnos(self):
        self.assertEqual(self.computacion.obtener_alumnos(), ['Franco','Lucas', 'Nehuen'])
class TestClaseProfesor(unittest.TestCase):
    def setUp(self):
        self.profepablo = Profesor('Pablo Gómez', 'Profesor', '121214')
    
    def testinit(self):
        self.assertEqual(self.profepablo.__nombre__, 'Pablo Gómez')
        self.assertEqual(self.profepablo.__cargo__, 'Profesor')
        self.assertEqual(self.profepablo.__legajo__, '121214')
    
    def testobtenernombre(self):
        self.assertEqual(self.profepablo.obtener_nombre(), 'Pablo Gómez')
    
    def testobtenercargo(self):
        self.assertEqual(self.profepablo.obtener_cargo(), 'Profesor')
    
    def testobtenerlegajo(self):
        self.assertEqual(self.profepablo.obtener_legajo(), '121214')
    
unittest.main()
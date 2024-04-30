import unittest

class Materia: # Agregar test para todos los métodos incluyendo el constructor
    def __init__(self, nombre, profesores, alumnos=[]):
        self.__nombre__ = nombre
        self.__profesores__ = profesores
        self.__alumnos__ = alumnos
    def obtener_profesores(self):
        return self.__profesores__
    def obtener_alumnos(self): #Obtiene el nombre de una clase Alumno
        lista_alumnos = []
        for estu in self.__alumnos__: 
            lista_alumnos.append(estu.__nombre__)
        return lista_alumnos
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
        

class TestClaseAlumnos(unittest.TestCase):
    def setUp(self) -> None:
        self.alumno = Alumno('Franco','Ing Inf', 45)
    
    def testinit(self):
        self.assertEqual(self.alumno.__nombre__, 'Franco')
        self.assertEqual(self.alumno.__carrera__, 'Ing Inf')
        self.assertEqual(self.alumno.__puntos__, 45)

class TestclaseMateria(unittest.TestCase):
    def setUp(self):
        self.alumnado = [Alumno('Franco','Ing Inf', 45), Alumno('Lucas','Ing Inf', 33),Alumno('Nehuen','Ing Inf', 40)]
        self.computacion = Materia('Computación', ['Elio', 'Walter', 'Daniel', 'Gabriel'], self.alumnado)
        #computacion = Materia('Computación', ['Elio', 'Walter', 'Daniel', 'Gabriel'])
    def testinit(self):
        self.assertEqual(self.computacion.__nombre__, 'Computación')
        self.assertEqual(self.computacion.__profesores__, ['Elio', 'Walter', 'Daniel', 'Gabriel'])
        self.assertEqual(self.computacion.__alumnos__, self.alumnado) #Test que comprueba la lista de clases de alumnos(self.alumnado)

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
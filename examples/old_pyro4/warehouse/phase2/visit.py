# This is the code that visits the warehouse.
from Pyro5.compatibility import Pyro4
import Pyro4
from person import Person


uri = input("Enter the uri of the warehouse: ").strip()
warehouse = Pyro4.Proxy(uri)
janet = Person("Janet")
henry = Person("Henry")
janet.visit(warehouse)
henry.visit(warehouse)

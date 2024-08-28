import os
import math
import decimal
from decimal import Decimal, getcontext
import Characters
from Characters import J7PhysicsLogo

# Things necessary for the code
getcontext().prec = 50
SelectedUnit = "meter"

# Units Nested Dictionary
Units = {
    "foot": {
      "name": "foot",
      "active": False,
      "value": 0.3048
    },
    "yard": {
      "name": "yard(s)",
      "active": False,
      "value": 0.9144
    },
    "inch": {
      "name": "inch(es)",
      "active": False,
      "value": 0.0254
    },
    "centimeter": {
      "name": "centimeter(s)",
      "active": False,
      "value": 0.01
    },
    "meter": {
      "name": "meter(s)",
      "active": True,
      "value": 1
    },
}

def Exit():
  # Gives the exit prompt
  ExitInput = input("\nType anything to leave")
  os.system('clear') 

def Instructions():
  # Instructions on how to use the program
  os.system('clear')
  print("Welcome to J7Physics! These are the basic instructions/information you will need to know to use it"), '\n', print("\n1. This converts the x1, x2, y1, and y2 and both angles of your desired 2 triangles."), '\n', print("\n2. Selecting a specific unit ONLY converts the resultant into that specific unit."), '\n', print("\n3. The default unit is meters and you must input your x1, x2, y1, and y2 in meters. ")
  Exit()

def UnitSelection():
    # Unit selection
    global SelectedUnit

    os.system('clear')
    print("\nCONVERTED RESULTANT UNIT SELECTIONS: \nFoot | Yard | Inch | Centimeter | Meter")

    UnitSelectionInput = input("\nInput desired unit: ").lower()
    SelectedUnit = str(UnitSelectionInput)

    if UnitSelectionInput in Units:
      for unit in Units:
          Units[unit]['active'] = False

      Units[SelectedUnit]['active'] = True

      SelectedUnit = UnitSelectionInput


def Caculation():
  #Function variables
  global SelectedUnit
  os.system('clear')
  AngleLoop = True

  #X, Y, and Z inputs
  InputX1 = float(input("\nx1: "))
  InputX2 = float(input("\nx2: "))
  Inputy1 = float(input("\ny1: "))
  Inputy2 = float(input("\ny2: "))
  
  Angle1Input = float(input("\n1st Angle: "))
  Angle2Input = float(input("\n2nd Angle: "))

  MagnitudeSolution = ((InputX1) ** 2 + (Inputy1) ** 2)**0.5
  MagnitudeSolution2 = ((InputX2) ** 2 + (Inputy2) ** 2)**0.5
  # Finding the resultant
  Rx = InputX1 + InputX2
  Ry = Inputy1 + Inputy2

  Resultant = ((Rx)**2 + (Ry)**2)**0.5

  def UnitCalculation():
    #Sub function that creates a message and prints it with the resultant and angle 
    if Units[SelectedUnit]['active'] == True:
      ResultantUnitConvert = (Resultant*(Units[SelectedUnit]['value']))

      ResultantAngle = math.degrees(math.atan((Inputy1+Inputy2) / (InputX1+InputX2)))


      print(f"\nYour Resultant is {ResultantUnitConvert} {Units[SelectedUnit]['name']} and the resultant angle is {ResultantAngle} degrees")

  UnitCalculation()

  Exit()

while True:
  # Menu
  os.system('clear')

  print(J7PhysicsLogo),print("\n<------------------------------------------------------------>") ,'\n', print("'c': Calculate"), '\n', print("'us': Unit Settings"), '\n', print("'i': Instructions")

  MenuInput = input("\n[TYPE]>")

  match MenuInput.lower():
    case "c":
      Caculation()

    case "us":
      UnitSelection()

    case "i":
      Instructions()

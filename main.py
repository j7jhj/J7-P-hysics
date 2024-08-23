import os
import math

# CHECKLIST: Caculate displacement/velocity, unit selection, decorate
# Math things needed: math.atan(), math.cos(), math.sin()

Units = {
    "foot": False,
    "yard": False,
    "inch": False,
    "centimeter": False,
    "meter": True,
}

def Exit():
  # Gives the exit prompt
  ExitInput = input("\nType anything to leave")
  os.system('clear') 

def UnitSelection():
    # Unit selection
    os.system('clear')
    print("\nCONVERTED UNIT SELECTIONS: \nFoot | Yard | Inch | Centimeter | Meter")

    UnitSelectionInput = input("\nInput desired unit: ").lower()

    if UnitSelectionInput is not None:
        Units.update({'foot': False, "yard": False, "inch": False, "centimeter": False, "meter": False})
        Units[UnitSelectionInput] = True

def EliasDoesntKnowTruePeak():
  global UnitSelectionInput
  #X, Y, and Z inputs
  InputX = int(input("\nX: "))
  InputY = int(input("\nY: "))
  TimeInput = int(input("\nTime: "))

  DeplaceAdd = (((InputX) ** 2) + ((InputY** 2)))**0.5

  Velocity = ((DeplaceAdd) / (TimeInput))


  def unitCacultion():
    if Units['foot'] == True:
        Displacement = (DeplaceAdd * 3.28084)

        print(f"\nYour displacement is {Displacement} foot and your Velocity is {Velocity} m/s")

    elif Units['yard'] == True:
        Displacement = (DeplaceAdd * 1.0936133333333)

        print(f"\nYour displacement is {Displacement} yard(s) and your Velocity is {Velocity} m/s")

    elif Units['inch'] == True:
        Displacement = (DeplaceAdd * 39.370079999998800702)

        print(f"\nYour displacement is {Displacement} inch(es) and your Velocity is {Velocity} m/s")

    elif Units['centimeter'] == True:
        Displacement = (DeplaceAdd * 100.00000319999695364)

        print(f"\nYour displacement is {Displacement} centimeter(s) and your Velocity is {Velocity} m/s")

    elif Units['meter'] == True:
        Displacement = (DeplaceAdd * 1)

        print(f"\nYour displacement is {Displacement} meter(s) and your Velocity is {Velocity} m/s")

  unitCacultion()

  Exit()

while True:
  # Menu
  os.system('clear')
  
  print("Welcome to J7(P)hysics! | Ver. ALPHA"), '\n', print("(c): Caculate"), '\n', print("(us): Unit Selection")

  MenuInput = input("\n[TYPE]>")

  match MenuInput.lower():
    case "c":
      EliasDoesntKnowTruePeak()

    case "us":
      UnitSelection()

  
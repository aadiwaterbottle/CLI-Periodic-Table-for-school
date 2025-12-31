import time
import sys

h = "\33[92m"+'H'+"\33[0m"

def periodic_table():# periodic table
    print(f"Non Metals:\n"
          f"{"\33[92m"+'Reactive Non-metals'+"\33[0m"}\n"
          f"{"\33[35m"+'Noble Gases'+"\33[0m"}\n"
          f"Metals:\n"
          f"{"\33[31m"+'Alkali metals'+"\33[0m"}\n"
          f"{'\33[36m'+ 'Alkaline earth metals'+"\33[0m"}\n"
          f"{'\33[47m'+ 'Lanthanoids'+"\33[0m"}\n"
          f"{'\33[45m'+'Actinoids'+"\33[0m"}\n"
          f"{'\33[37m'+'Transition Metals'+"\33[0m"}\n"
          f"{'\33[33m'+'Post-Transition Metals'+"\33[0m"}\n"
          f"Neither:\n"
          f"{'\33[34m'+'Metalloids'+"\33[0m"}\n")
    print(f"__________                                                                                                                                                      __________\n"
        f"|    1   |                                                                                                                                                      |    2   |\n"
        f"|    {h}   |""                                                                                                                                                      ""|   He   |\n"
        f"|________|_________                                                                                                _____________________________________________|________|\n"
        f"|    3   |    4   |                                                                                                |   5    |   6    |    7   |    8   |    9   |   10   |\n"
        f"|   Li   |   Be   |                                                                                                |   B    |   C    |    N   |    O   |    F   |   Ne   |\n"
        f"|________|________|                                                                                                |________|________|________|________|________|________|\n"
        f"|   11   |   12   |                                                                                                |   13   |   14   |   15   |   16   |   17   |   18   |\n"
        f"|   Na   |   Mg   |                                                                                                |   Al   |   Si   |   P    |    S   |   Cl   |   Ar   |\n"
        f"|________|________|_________      _________________________________________________________________________________|________|________|________|________|________|________|\n"
        f"|   19   |   20   |   21   |      |   22   |   23   |   24   |   25   |   26   |   27   |   28   |   29   |   30   |   31   |   32   |   33   |   34   |   35   |   36   |\n"
        f"|    K   |   Ca   |   Sc   |      |   Ti   |   V    |   Cr   |   Mn   |   Fe   |   Co   |   Ni   |   Cu   |   Zn   |   Ga   |   Ge   |   As   |   Se   |   Br   |   Kr   |\n"
        f"|________|________|________|      |________|________|________|________|________|________|________|________|________|________|________|________|________|________|________|\n"
        f"|   37   |   38   |   39   |      |   40   |   41   |   42   |   43   |   44   |   45   |   46   |   47   |   48   |   49   |        |        |        |        |        |\n"
        f"|   Rb   |   Sr   |   Y    |      |   Zr   |   Nb   |   Mo   |   Tc   |   Ru   |   Rh   |   Pd   |   Ag   |   Cd   |   In   |   Sn   |   Sb   |   Te   |    I   |   Xe   |\n"
        f"|________|________|________|      |________|________|________|________|________|________|________|________|________|________|________|________|________|________|________|\n"
        f"|        |        |        |      |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |\n"
        f"|   Cs   |   Ba   |   La   |      |   Hf   |   Ta   |    W   |   Re   |   Os   |   Ir   |   Pt   |   Au   |   Hg   |   Tl   |   Pb   |   Bi   |   Po   |   At   |   Rn   |\n"
        f"|________|________|________|      |________|________|________|________|________|________|________|________|________|________|________|________|________|________|________|\n"
        f"|        |        |        |      |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |\n"
        f"|   Fr   |   Ra   |   Ac   |      |   Rf   |   Db   |   Sg   |   Bh   |   Hs   |   Mt   |   Ds   |   Rg   |   Cn   |   Nh   |   Fl   |   Mc   |   Lv   |   Ts   |   Og   |\n"
        f"|________|________|________|      |________|________|________|________|________|________|________|________|________|________|________|________|________|________|________|\n"
        f"\n"
        f"                                  _______________________________________________________________________________________________________________________________\n"
        f"                                  |        |        |        |        |        |        |        |        |        |        |        |        |        |        |\n"
        f"                                  |        |        |        |        |        |        |        |        |        |        |        |        |        |        |\n"
        f"                                  |________|________|________|________|________|________|________|________|________|________|________|________|________|________|\n"
        f"                                  |        |        |        |        |        |        |        |        |        |        |        |        |        |        |\n"
        f"                                  |        |        |        |        |        |        |        |        |        |        |        |        |        |        |\n"
        f"                                  |________|________|________|________|________|________|________|________|________|________|________|________|________|________|\n"
        "")
    return

def slow_type(text):  # Makes a typewriter effect when outputting
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05) # Adjust the delay for typing speed
    return



slow_type(f"Please wait for table to load...{time.sleep(5)}\r")

slow_type(f"Table Loaded!\r")

slow_type("Periodic Table [for a list of commands type help]\n")
while True:
    command = input(">>>")
    if command == "!p table":
        slow_type(f"Extracting elements...\r")
        #time.sleep(5)
        slow_type(f"Elements Extracted!\r")
        periodic_table()
    if command == "help":
        slow_type("Okay! Here's the list of commands.\n help\n")
        print("help\n!p table\n!p (any element)\n!p series\nexit")
    elif command == "exit":
        break
    elif command == 'a':
        slow_type("a")

import time
import sys

periodic_elements = {
    "H":  {"name": "Hydrogen", "number": 1, "weight": 1.008},
    "He": {"name": "Helium", "number": 2, "weight": 4.0026},
    "Li": {"name": "Lithium", "number": 3, "weight": 6.94},
    "Be": {"name": "Beryllium", "number": 4, "weight": 9.0122},
    "B":  {"name": "Boron", "number": 5, "weight": 10.81},
    "C":  {"name": "Carbon", "number": 6, "weight": 12.011},
    "N":  {"name": "Nitrogen", "number": 7, "weight": 14.007},
    "O":  {"name": "Oxygen", "number": 8, "weight": 15.999},
    "F":  {"name": "Fluorine", "number": 9, "weight": 18.998},
    "Ne": {"name": "Neon", "number": 10, "weight": 20.180},
    "Na": {"name": "Sodium", "number": 11, "weight": 22.990},
    "Mg": {"name": "Magnesium", "number": 12, "weight": 24.305},
    "Al": {"name": "Aluminum", "number": 13, "weight": 26.982},
    "Si": {"name": "Silicon", "number": 14, "weight": 28.085},
    "P":  {"name": "Phosphorus", "number": 15, "weight": 30.974},
    "S":  {"name": "Sulfur", "number": 16, "weight": 32.06},
    "Cl": {"name": "Chlorine", "number": 17, "weight": 35.45},
    "Ar": {"name": "Argon", "number": 18, "weight": 39.948},
    "K":  {"name": "Potassium", "number": 19, "weight": 39.098},
    "Ca": {"name": "Calcium", "number": 20, "weight": 40.078},
    "Sc": {"name": "Scandium", "number": 21, "weight": 44.956},
    "Ti": {"name": "Titanium", "number": 22, "weight": 47.867},
    "V":  {"name": "Vanadium", "number": 23, "weight": 50.942},
    "Cr": {"name": "Chromium", "number": 24, "weight": 51.996},
    "Mn": {"name": "Manganese", "number": 25, "weight": 54.938},
    "Fe": {"name": "Iron", "number": 26, "weight": 55.845},
    "Co": {"name": "Cobalt", "number": 27, "weight": 58.933},
    "Ni": {"name": "Nickel", "number": 28, "weight": 58.693},
    "Cu": {"name": "Copper", "number": 29, "weight": 63.546},
    "Zn": {"name": "Zinc", "number": 30, "weight": 65.38},
    "Ga": {"name": "Gallium", "number": 31, "weight": 69.723},
    "Ge": {"name": "Germanium", "number": 32, "weight": 72.630},
    "As": {"name": "Arsenic", "number": 33, "weight": 74.922},
    "Se": {"name": "Selenium", "number": 34, "weight": 78.96},
    "Br": {"name": "Bromine", "number": 35, "weight": 79.904},
    "Kr": {"name": "Krypton", "number": 36, "weight": 83.798},
    "Rb": {"name": "Rubidium", "number": 37, "weight": 85.468},
    "Sr": {"name": "Strontium", "number": 38, "weight": 87.62},
    "Y":  {"name": "Yttrium", "number": 39, "weight": 88.906},
    "Zr": {"name": "Zirconium", "number": 40, "weight": 91.224},
    "Nb": {"name": "Niobium", "number": 41, "weight": 92.906},
    "Mo": {"name": "Molybdenum", "number": 42, "weight": 95.95},
    "Tc": {"name": "Technetium", "number": 43, "weight": 98},
    "Ru": {"name": "Ruthenium", "number": 44, "weight": 101.07},
    "Rh": {"name": "Rhodium", "number": 45, "weight": 102.91},
    "Pd": {"name": "Palladium", "number": 46, "weight": 106.42},
    "Ag": {"name": "Silver", "number": 47, "weight": 107.87},
    "Cd": {"name": "Cadmium", "number": 48, "weight": 112.41},
    "In": {"name": "Indium", "number": 49, "weight": 114.82},
    "Sn": {"name": "Tin", "number": 50, "weight": 118.71},
    "Sb": {"name": "Antimony", "number": 51, "weight": 121.76},
    "Te": {"name": "Tellurium", "number": 52, "weight": 127.60},
    "I":  {"name": "Iodine", "number": 53, "weight": 126.90},
    "Xe": {"name": "Xenon", "number": 54, "weight": 131.29},
    "Cs": {"name": "Cesium", "number": 55, "weight": 132.91},
    "Ba": {"name": "Barium", "number": 56, "weight": 137.33},
    "La": {"name": "Lanthanum", "number": 57, "weight": 138.91},
    "Ce": {"name": "Cerium", "number": 58, "weight": 140.12},
    "Pr": {"name": "Praseodymium", "number": 59, "weight": 140.91},
    "Nd": {"name": "Neodymium", "number": 60, "weight": 144.24},
    "Pm": {"name": "Promethium", "number": 61, "weight": 145},
    "Sm": {"name": "Samarium", "number": 62, "weight": 150.36},
    "Eu": {"name": "Europium", "number": 63, "weight": 151.96},
    "Gd": {"name": "Gadolinium", "number": 64, "weight": 157.25},
    "Tb": {"name": "Terbium", "number": 65, "weight": 158.93},
    "Dy": {"name": "Dysprosium", "number": 66, "weight": 162.50},
    "Ho": {"name": "Holmium", "number": 67, "weight": 164.93},
    "Er": {"name": "Erbium", "number": 68, "weight": 167.26},
    "Tm": {"name": "Thulium", "number": 69, "weight": 168.93},
    "Yb": {"name": "Ytterbium", "number": 70, "weight": 173.05},
    "Lu": {"name": "Lutetium", "number": 71, "weight": 174.97},
    "Hf": {"name": "Hafnium", "number": 72, "weight": 178.49},
    "Ta": {"name": "Tantalum", "number": 73, "weight": 180.95},
    "W":  {"name": "Tungsten", "number": 74, "weight": 183.84},
    "Re": {"name": "Rhenium", "number": 75, "weight": 186.21},
    "Os": {"name": "Osmium", "number": 76, "weight": 190.23},
    "Ir": {"name": "Iridium", "number": 77, "weight": 192.22},
    "Pt": {"name": "Platinum", "number": 78, "weight": 195.08},
    "Au": {"name": "Gold", "number": 79, "weight": 196.97},
    "Hg": {"name": "Mercury", "number": 80, "weight": 200.59},
    "Tl": {"name": "Thallium", "number": 81, "weight": 204.38},
    "Pb": {"name": "Lead", "number": 82, "weight": 207.2},
    "Bi": {"name": "Bismuth", "number": 83, "weight": 208.98},
    "Po": {"name": "Polonium", "number": 84, "weight": 209},
    "At": {"name": "Astatine", "number": 85, "weight": 210},
    "Rn": {"name": "Radon", "number": 86, "weight": 222},
    "Fr": {"name": "Francium", "number": 87, "weight": 223},
    "Ra": {"name": "Radium", "number": 88, "weight": 226},
    "Ac": {"name": "Actinium", "number": 89, "weight": 227},
    "Th": {"name": "Thorium", "number": 90, "weight": 232.04},
    "Pa": {"name": "Protactinium", "number": 91, "weight": 231.04},
    "U":  {"name": "Uranium", "number": 92, "weight": 238.03},
    "Np": {"name": "Neptunium", "number": 93, "weight": 237},
    "Pu": {"name": "Plutonium", "number": 94, "weight": 244},
    "Am": {"name": "Americium", "number": 95, "weight": 243},
    "Cm": {"name": "Curium", "number": 96, "weight": 247},
    "Bk": {"name": "Berkelium", "number": 97, "weight": 247},
    "Cf": {"name": "Californium", "number": 98, "weight": 251},
    "Es": {"name": "Einsteinium", "number": 99, "weight": 252},
    "Fm": {"name": "Fermium", "number": 100, "weight": 257},
    "Md": {"name": "Mendelevium", "number": 101, "weight": 258},
    "No": {"name": "Nobelium", "number": 102, "weight": 259},
    "Lr": {"name": "Lawrencium", "number": 103, "weight": 266},
    "Rf": {"name": "Rutherfordium", "number": 104, "weight": 267},
    "Db": {"name": "Dubnium", "number": 105, "weight": 268},
    "Sg": {"name": "Seaborgium", "number": 106, "weight": 269},
    "Bh": {"name": "Bohrium", "number": 107, "weight": 270},
    "Hs": {"name": "Hassium", "number": 108, "weight": 277},
    "Mt": {"name": "Meitnerium", "number": 109, "weight": 278},
    "Ds": {"name": "Darmstadtium", "number": 110, "weight": 281},
    "Rg": {"name": "Roentgenium", "number": 111, "weight": 282},
    "Cn": {"name": "Copernicium", "number": 112, "weight": 285},
    "Nh": {"name": "Nihonium", "number": 113, "weight": 286},
    "Fl": {"name": "Flerovium", "number": 114, "weight": 289},
    "Mc": {"name": "Moscovium", "number": 115, "weight": 290},
    "Lv": {"name": "Livermorium", "number": 116, "weight": 293},
    "Ts": {"name": "Tennessine", "number": 117, "weight": 294},
    "Og": {"name": "Oganesson", "number": 118, "weight": 294}
}

def periodic_series(): # the series the elements fall under
    print(f"Non Metals:\n"
          f"{"\33[92m" + 'Reactive Non-metals' + "\33[0m"}\n"
          f"{"\33[35m" + 'Noble Gases' + "\33[0m"}\n"
          f"Metals:\n"
          f"{"\33[31m" + 'Alkali metals' + "\33[0m"}\n"
          f"{'\33[36m' + 'Alkaline earth metals' + "\33[0m"}\n"
          f"{'\33[47m' + 'Lanthanoids' + "\33[0m"}\n"
          f"{'\33[45m' + 'Actinoids' + "\33[0m"}\n"
          f"{'\33[90m' + 'Transition Metals' + "\33[0m"}\n"
          f"{'\33[33m' + 'Post-Transition Metals' + "\33[0m"}\n"
          f"Neither:\n"
          f"{'\33[34m' + 'Metalloids' + "\33[0m"}\n"
          f"{'\33[97m' + 'Unknown' + '\33[0m'}")
    return

def periodic_table():# periodic table
    print(f"__________                                                                                                                                                        __________\n"
        f"|    1   |                                                                                                                                                        |    2   |\n"
        f"|    {"\33[92m"+'H'+"\33[0m"}   |""                                                                                                                                                        "f"|   {"\33[35m" + 'He' + "\33[0m"}   |\n"
        f"|________|_________                                                                                                  _____________________________________________|________|\n"
        f"|    3   |    4   |                                                                                                  |   5    |   6    |    7   |    8   |    9   |   10   |\n"
        f"|   {"\33[31m" + 'Li' + "\33[0m"}   |   {'\33[36m' + 'Be' + "\33[0m"}   |                                                                                                  |   {'\33[34m' + 'B' + "\33[0m"}    |   {"\33[92m"+'C'+"\33[0m"}    |    {"\33[92m"+'N'+"\33[0m"}   |    {"\33[92m"+'O'+"\33[0m"}   |    {"\33[92m"+'F'+"\33[0m"}   |   {"\33[35m" + 'Ne' + "\33[0m"}   |\n"
        f"|________|________|                                                                                                  |________|________|________|________|________|________|\n"
        f"|   11   |   12   |                                                                                                  |   13   |   14   |   15   |   16   |   17   |   18   |\n"
        f"|   {"\33[31m" + 'Na' + "\33[0m"}   |   {'\33[36m' + 'Mg' + "\33[0m"}   |                                                                                                  |   {'\33[33m' + 'Al' + "\33[0m"}   |   {'\33[34m' + 'Si' + "\33[0m"}   |   {"\33[92m"+'P'+"\33[0m"}    |    {"\33[92m"+'S'+"\33[0m"}   |   {"\33[92m"+'Cl'+"\33[0m"}   |   {"\33[35m" + 'Ar' + "\33[0m"}   |\n"
        f"|________|________|        __________________________________________________________________________________________|________|________|________|________|________|________|\n"
        f"|   19   |   20   |        |   21   |   22   |   23   |   24   |   25   |   26   |   27   |   28   |   29   |   30   |   31   |   32   |   33   |   34   |   35   |   36   |\n"
        f"|    {"\33[31m" + 'K' + "\33[0m"}   |   {'\33[36m' + 'Ca' + "\33[0m"}   |        |   {'\33[90m' + 'Sc' + "\33[0m"}   |   {'\33[90m' + 'Ti' + "\33[0m"}   |   {'\33[90m' + 'V' + "\33[0m"}    |   {'\33[90m' + 'Cr' + "\33[0m"}   |   {'\33[90m' + 'Mn' + "\33[0m"}   |   {'\33[90m' + 'Fe' + "\33[0m"}   |   {'\33[90m' + 'Co' + "\33[0m"}   |   {'\33[90m' + 'Ni' + "\33[0m"}   |   {'\33[90m' + 'Cu' + "\33[0m"}   |   {'\33[90m' + 'Zn' + "\33[0m"}   |   {'\33[33m' + 'Ga' + "\33[0m"}   |   {'\33[34m' + 'Ge' + "\33[0m"}   |   {'\33[34m' + 'As' + "\33[0m"}   |   {"\33[92m"+'Se'+"\33[0m"}   |   {"\33[92m"+'Br'+"\33[0m"}   |   {"\33[35m" + 'Kr' + "\33[0m"}   |\n"
        f"|________|________|        |________|________|________|________|________|________|________|________|________|________|________|________|________|________|________|________|\n"
        f"|   37   |   38   |        |   90   |   40   |   90   |   42   |   43   |   44   |   45   |   46   |   47   |   48   |   49   |   50   |   51   |   52   |   53   |   54   |\n"
        f"|   {"\33[31m" + 'Rb' + "\33[0m"}   |   {'\33[36m' + 'Sr' + "\33[0m"}   |        |   {'\33[90m' + 'Y' + "\33[0m"}    |   {'\33[90m' + 'Zr' + "\33[0m"}   |   {'\33[90m' + 'Nb' + "\33[0m"}   |   {'\33[90m' + 'Mo' + "\33[0m"}   |   {'\33[90m' + 'Tc' + "\33[0m"}   |   {'\33[90m' + 'Ru' + "\33[0m"}   |   {'\33[90m' + 'Rh' + "\33[0m"}   |   {'\33[90m' + 'Pd' + "\33[0m"}   |   {'\33[90m' + 'Ag' + "\33[0m"}   |   {'\33[90m' + 'Cd' + "\33[0m"}   |   {'\33[33m' + 'In' + "\33[0m"}   |   {'\33[33m' + 'Sn' + "\33[0m"}   |   {'\33[34m' + 'Sb' + "\33[0m"}   |   {'\33[34m' + 'Te' + "\33[0m"}   |    {"\33[92m"+'I'+"\33[0m"}   |   {"\33[35m" + 'Xe' + "\33[0m"}   |\n"
        f"|________|________|        |________|________|________|________|________|________|________|________|________|________|________|________|________|________|________|________|\n"
        f"|   55   |   56   |                 |   72   |   73   |   74   |   75   |   76   |   77   |   78   |   79   |   80   |   81   |   82   |   83   |   84   |   85   |   86   |\n"
        f"|   {"\33[31m" + 'Cs' + "\33[0m"}   |   {'\33[36m' + 'Ba' + "\33[0m"}   |                 |   {'\33[90m' + 'Hf' + "\33[0m"}   |   {'\33[90m' + 'Ta' + "\33[0m"}   |    {'\33[90m' + 'W' + "\33[0m"}   |   {'\33[90m' + 'Re' + "\33[0m"}   |   {'\33[90m' + 'Os' + "\33[0m"}   |   {'\33[90m' + 'Ir' + "\33[0m"}   |   {'\33[90m' + 'Pt' + "\33[0m"}   |   {'\33[90m' + 'Au' + "\33[0m"}   |   {'\33[90m' + 'Hg' + "\33[0m"}   |   {'\33[33m' + 'Tl' + "\33[0m"}   |   {'\33[33m' + 'Pb' + "\33[0m"}   |   {'\33[33m' + 'Bi' + "\33[0m"}   |   {'\33[33m' + 'Po' + "\33[0m"}   |   {'\33[34m' + 'At' + "\33[0m"}   |   {"\33[35m" + 'Rn' + "\33[0m"}   |\n"
        f"|________|________|                 |________|________|________|________|________|________|________|________|________|________|________|________|________|________|________|\n"
        f"|   87   |   88   |                 |  104   |   105  |   106  |   107  |   108  |   109  |   110  |   111  |   112  |   113  |   114  |   115  |   116  |   117  |   118  |\n"
        f"|   {"\33[31m" + 'Fr' + "\33[0m"}   |   {'\33[36m' + 'Ra' + "\33[0m"}   |                 |   {'\33[90m' + 'Rf' + "\33[0m"}   |   {'\33[90m' + 'Db' + "\33[0m"}   |   {'\33[90m' + 'Sg' + "\33[0m"}   |   {'\33[90m' + 'Bh' + "\33[0m"}   |   {'\33[90m' + 'Hs' + "\33[0m"}   |   {'\33[97m' + 'Mt' + '\33[0m'}   |   {'\33[97m' + 'Ds' + '\33[0m'}   |   {'\33[97m' + 'Rg' + '\33[0m'}   |   {'\33[97m' + 'Cn' + '\33[0m'}   |   {'\33[97m' + 'Nh' + '\33[0m'}   |   {'\33[97m' + 'Fl' + '\33[0m'}   |   {'\33[97m' + 'Mc' + '\33[0m'}   |   {'\33[97m' + 'Lv' + '\33[0m'}   |   {'\33[97m' + 'Ts' + '\33[0m'}   |   {'\33[97m' + 'Og' + '\33[0m'}   |\n"
        f"|________|________|                 |________|________|________|________|________|________|________|________|________|________|________|________|________|________|________|\n"
        f"\n"
        f"                           ________________________________________________________________________________________________________________________________________\n"
        f"                           |   57   |   58   |   59   |   60   |   61   |   62   |   63   |   64   |   65   |   66   |   67   |   68   |   69   |   70   |   71   |\n"
        f"                           |   {'\33[47m' + 'La' + "\33[0m"}   |   {'\33[47m' + 'Ce' + "\33[0m"}   |   {'\33[47m' + 'Pr' + "\33[0m"}   |   {'\33[47m' + 'Nd' + "\33[0m"}   |   {'\33[47m' + 'Pm' + "\33[0m"}   |   {'\33[47m' + 'Sm' + "\33[0m"}   |   {'\33[47m' + 'Eu' + "\33[0m"}   |   {'\33[47m' + 'Gd' + "\33[0m"}   |   {'\33[47m' + 'Tb' + "\33[0m"}   |   {'\33[47m' + 'dy' + "\33[0m"}   |   {'\33[47m' + 'Ho' + "\33[0m"}   |   {'\33[47m' + 'Er' + "\33[0m"}   |   {'\33[47m' + 'Tm' + "\33[0m"}   |   {'\33[47m' + 'Yb' + "\33[0m"}   |   {'\33[47m' + 'Lu' + "\33[0m"}   |\n"
        f"                           |________|________|________|________|________|________|________|________|________|________|________|________|________|________|________|\n"
        f"                           |   89   |   90   |   91   |   92   |   93   |   94   |   95   |   96   |   97   |   98   |   99   |  100   |  101   |  102   |  103   |\n"
        f"                           |   {'\33[45m' + 'Ac' + "\33[0m"}   |   {'\33[45m' + 'Th' + "\33[0m"}   |   {'\33[45m' + 'Pa' + "\33[0m"}   |   {'\33[45m' + 'U' + "\33[0m"}    |   {'\33[45m' + 'Np' + "\33[0m"}   |   {'\33[45m' + 'Pu' + "\33[0m"}   |   {'\33[45m' + 'Am' + "\33[0m"}   |   {'\33[45m' + 'Cm' + "\33[0m"}   |   {'\33[45m' + 'Bk' + "\33[0m"}   |   {'\33[45m' + 'Cd' + "\33[0m"}   |   {'\33[45m' + 'Es' + "\33[0m"}   |   {'\33[45m' + 'Fm' + "\33[0m"}   |   {'\33[45m' + 'Md' + "\33[0m"}   |   {'\33[45m' + 'No' + "\33[0m"}   |   {'\33[45m' + 'Lr' + "\33[0m"}   |\n"
        f"                           |________|________|________|________|________|________|________|________|________|________|________|________|________|________|________|\n"
        "")
    return

def slow_type(text):  # Makes a typewriter effect when outputting
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05) # Adjust the delay for typing speed
    return

def get_element_by_number(number):
    for symbol, details in periodic_elements.items():
        if details['number'] == number:
            return symbol, details
    return None

# Example: Find element 79
symbol, info = get_element_by_number(79)
print(f"Element 79 is {info['name']} ({symbol})")

slow_type("Periodic Table [for a list of commands type help]\n")
while True:
    command = input(">>>")
    if command == "!p table":
        periodic_series()
        periodic_table()
    elif command == "help":
        slow_type("Okay! Here's the list of commands.\n help\n")
        print("help\n!p table\n!p element (symbol, name or atomic number e.g. Au or Gold or 79)\n!p series\n!p period\nexit")
    elif command == "exit":
        break
    elif command == 'a':
        slow_type("a")
    elif command == '!p series':
        periodic_series()
        slow_type("Would you like to know more about the series? (Input a series or input y for all, n for no)\n")
        a = input(">>>")
        if a == "y":
            slow_type("AWESOME")
        elif a == "Reactive Non-metals":
            slow_type("Reactive Non-metals")
        elif a == "Noble Gases":
            slow_type("Noble Gases")
        elif a == "Alkali metals":
            slow_type("Alkali metals")
        elif a == "Lanthanoids":
            slow_type("Lanthanoids")
        elif a == "Actinoids":
            slow_type("Actinoids")
        elif a == "Transition Metals":
            slow_type("Transition Metals")
        elif a == "Post-Transition Metals":
            slow_type("Post-Transition Metals")
        elif a == "Metalloids":
            slow_type("Metalloids")
        elif a == "Unknown":
            slow_type("Unknown")
    elif command == "!p period":
        slow_type("period")

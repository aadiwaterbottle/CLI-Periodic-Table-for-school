import time
import sys

periodic_elements = { # the dictionary for the elements
    "H":  {"name": "Hydrogen", "number": 1, "weight": 1.008, "shells": [1]},
    "He": {"name": "Helium", "number": 2, "weight": 4.0026, "shells": [2]},
    "Li": {"name": "Lithium", "number": 3, "weight": 6.94, "shells": [2, 1]},
    "Be": {"name": "Beryllium", "number": 4, "weight": 9.0122, "shells": [2, 2]},
    "B":  {"name": "Boron", "number": 5, "weight": 10.81, "shells": [2, 3]},
    "C":  {"name": "Carbon", "number": 6, "weight": 12.011, "shells": [2, 4]},
    "N":  {"name": "Nitrogen", "number": 7, "weight": 14.007, "shells": [2, 5]},
    "O":  {"name": "Oxygen", "number": 8, "weight": 15.999, "shells": [2, 6]},
    "F":  {"name": "Fluorine", "number": 9, "weight": 18.998, "shells": [2, 7]},
    "Ne": {"name": "Neon", "number": 10, "weight": 20.180, "shells": [2, 8]},
    "Na": {"name": "Sodium", "number": 11, "weight": 22.990, "shells": [2, 8, 1]},
    "Mg": {"name": "Magnesium", "number": 12, "weight": 24.305, "shells": [2, 8, 2]},
    "Al": {"name": "Aluminum", "number": 13, "weight": 26.982, "shells": [2, 8, 3]},
    "Si": {"name": "Silicon", "number": 14, "weight": 28.085, "shells": [2, 8, 4]},
    "P":  {"name": "Phosphorus", "number": 15, "weight": 30.974, "shells": [2, 8, 5]},
    "S":  {"name": "Sulfur", "number": 16, "weight": 32.06, "shells": [2, 8, 6]},
    "Cl": {"name": "Chlorine", "number": 17, "weight": 35.45, "shells": [2, 8, 7]},
    "Ar": {"name": "Argon", "number": 18, "weight": 39.948, "shells": [2, 8, 8]},
    "K":  {"name": "Potassium", "number": 19, "weight": 39.098, "shells": [2, 8, 8, 1]},
    "Ca": {"name": "Calcium", "number": 20, "weight": 40.078, "shells": [2, 8, 8, 2]},
    "Sc": {"name": "Scandium", "number": 21, "weight": 44.956, "shells": [2, 8, 9, 2]},
    "Ti": {"name": "Titanium", "number": 22, "weight": 47.867, "shells": [2, 8, 10, 2]},
    "V":  {"name": "Vanadium", "number": 23, "weight": 50.942, "shells": [2, 8, 11, 2]},
    "Cr": {"name": "Chromium", "number": 24, "weight": 51.996, "shells": [2, 8, 13, 1]},
    "Mn": {"name": "Manganese", "number": 25, "weight": 54.938, "shells": [2, 8, 13, 2]},
    "Fe": {"name": "Iron", "number": 26, "weight": 55.845, "shells": [2, 8, 14, 2]},
    "Co": {"name": "Cobalt", "number": 27, "weight": 58.933, "shells": [2, 8, 15, 2]},
    "Ni": {"name": "Nickel", "number": 28, "weight": 58.693, "shells": [2, 8, 16, 2]},
    "Cu": {"name": "Copper", "number": 29, "weight": 63.546, "shells": [2, 8, 18, 1]},
    "Zn": {"name": "Zinc", "number": 30, "weight": 65.38, "shells": [2, 8, 18, 2]},
    "Ga": {"name": "Gallium", "number": 31, "weight": 69.723, "shells": [2, 8, 18, 3]},
    "Ge": {"name": "Germanium", "number": 32, "weight": 72.630, "shells": [2, 8, 18, 4]},
    "As": {"name": "Arsenic", "number": 33, "weight": 74.922, "shells": [2, 8, 18, 5]},
    "Se": {"name": "Selenium", "number": 34, "weight": 78.96, "shells": [2, 8, 18, 6]},
    "Br": {"name": "Bromine", "number": 35, "weight": 79.904, "shells": [2, 8, 18, 7]},
    "Kr": {"name": "Krypton", "number": 36, "weight": 83.798, "shells": [2, 8, 18, 8]},
    "Rb": {"name": "Rubidium", "number": 37, "weight": 85.468, "shells": [2, 8, 18, 8, 1]},
    "Sr": {"name": "Strontium", "number": 38, "weight": 87.62, "shells": [2, 8, 18, 8, 2]},
    "Y":  {"name": "Yttrium", "number": 39, "weight": 88.906, "shells": [2, 8, 18, 9, 2]},
    "Zr": {"name": "Zirconium", "number": 40, "weight": 91.224, "shells": [2, 8, 18, 10, 2]},
    "Nb": {"name": "Niobium", "number": 41, "weight": 92.906, "shells": [2, 8, 18, 12, 1]},
    "Mo": {"name": "Molybdenum", "number": 42, "weight": 95.95, "shells": [2, 8, 18, 13, 1]},
    "Tc": {"name": "Technetium", "number": 43, "weight": 98, "shells": [2, 8, 18, 13, 2]},
    "Ru": {"name": "Ruthenium", "number": 44, "weight": 101.07, "shells": [2, 8, 18, 15, 1]},
    "Rh": {"name": "Rhodium", "number": 45, "weight": 102.91, "shells": [2, 8, 18, 16, 1]},
    "Pd": {"name": "Palladium", "number": 46, "weight": 106.42, "shells": [2, 8, 18, 18]},
    "Ag": {"name": "Silver", "number": 47, "weight": 107.87, "shells": [2, 8, 18, 18, 1]},
    "Cd": {"name": "Cadmium", "number": 48, "weight": 112.41, "shells": [2, 8, 18, 18, 2]},
    "In": {"name": "Indium", "number": 49, "weight": 114.82, "shells": [2, 8, 18, 18, 3]},
    "Sn": {"name": "Tin", "number": 50, "weight": 118.71, "shells": [2, 8, 18, 18, 4]},
    "Sb": {"name": "Antimony", "number": 51, "weight": 121.76, "shells": [2, 8, 18, 18, 5]},
    "Te": {"name": "Tellurium", "number": 52, "weight": 127.60, "shells": [2, 8, 18, 18, 6]},
    "I":  {"name": "Iodine", "number": 53, "weight": 126.90, "shells": [2, 8, 18, 18, 7]},
    "Xe": {"name": "Xenon", "number": 54, "weight": 131.29, "shells": [2, 8, 18, 18, 8]},
    "Cs": {"name": "Cesium", "number": 55, "weight": 132.91, "shells": [2, 8, 18, 18, 8, 1]},
    "Ba": {"name": "Barium", "number": 56, "weight": 137.33, "shells": [2, 8, 18, 18, 8, 2]},
    "La": {"name": "Lanthanum", "number": 57, "weight": 138.91, "shells": [2, 8, 18, 18, 9, 2]},
    "Ce": {"name": "Cerium", "number": 58, "weight": 140.12, "shells": [2, 8, 18, 19, 9, 2]},
    "Pr": {"name": "Praseodymium", "number": 59, "weight": 140.91, "shells": [2, 8, 18, 21, 8, 2]},
    "Nd": {"name": "Neodymium", "number": 60, "weight": 144.24, "shells": [2, 8, 18, 22, 8, 2]},
    "Pm": {"name": "Promethium", "number": 61, "weight": 145, "shells": [2, 8, 18, 23, 8, 2]},
    "Sm": {"name": "Samarium", "number": 62, "weight": 150.36, "shells": [2, 8, 18, 24, 8, 2]},
    "Eu": {"name": "Europium", "number": 63, "weight": 151.96, "shells": [2, 8, 18, 25, 8, 2]},
    "Gd": {"name": "Gadolinium", "number": 64, "weight": 157.25, "shells": [2, 8, 18, 25, 9, 2]},
    "Tb": {"name": "Terbium", "number": 65, "weight": 158.93, "shells": [2, 8, 18, 27, 8, 2]},
    "Dy": {"name": "Dysprosium", "number": 66, "weight": 162.50, "shells": [2, 8, 18, 28, 8, 2]},
    "Ho": {"name": "Holmium", "number": 67, "weight": 164.93, "shells": [2, 8, 18, 29, 8, 2]},
    "Er": {"name": "Erbium", "number": 68, "weight": 167.26, "shells": [2, 8, 18, 30, 8, 2]},
    "Tm": {"name": "Thulium", "number": 69, "weight": 168.93, "shells": [2, 8, 18, 31, 8, 2]},
    "Yb": {"name": "Ytterbium", "number": 70, "weight": 173.05, "shells": [2, 8, 18, 32, 8, 2]},
    "Lu": {"name": "Lutetium", "number": 71, "weight": 174.97, "shells": [2, 8, 18, 32, 9, 2]},
    "Hf": {"name": "Hafnium", "number": 72, "weight": 178.49, "shells": [2, 8, 18, 32, 10, 2]},
    "Ta": {"name": "Tantalum", "number": 73, "weight": 180.95, "shells": [2, 8, 18, 32, 11, 2]},
    "W":  {"name": "Tungsten", "number": 74, "weight": 183.84, "shells": [2, 8, 18, 32, 12, 2]},
    "Re": {"name": "Rhenium", "number": 75, "weight": 186.21, "shells": [2, 8, 18, 32, 13, 2]},
    "Os": {"name": "Osmium", "number": 76, "weight": 190.23, "shells": [2, 8, 18, 32, 14, 2]},
    "Ir": {"name": "Iridium", "number": 77, "weight": 192.22, "shells": [2, 8, 18, 32, 15, 2]},
    "Pt": {"name": "Platinum", "number": 78, "weight": 195.08, "shells": [2, 8, 18, 32, 17, 1]},
    "Au": {"name": "Gold", "number": 79, "weight": 196.97, "shells": [2, 8, 18, 32, 18, 1]},
    "Hg": {"name": "Mercury", "number": 80, "weight": 200.59, "shells": [2, 8, 18, 32, 18, 2]},
    "Tl": {"name": "Thallium", "number": 81, "weight": 204.38, "shells": [2, 8, 18, 32, 18, 3]},
    "Pb": {"name": "Lead", "number": 82, "weight": 207.2, "shells": [2, 8, 18, 32, 18, 4]},
    "Bi": {"name": "Bismuth", "number": 83, "weight": 208.98, "shells": [2, 8, 18, 32, 18, 5]},
    "Po": {"name": "Polonium", "number": 84, "weight": 209, "shells": [2, 8, 18, 32, 18, 6]},
    "At": {"name": "Astatine", "number": 85, "weight": 210, "shells": [2, 8, 18, 32, 18, 7]},
    "Rn": {"name": "Radon", "number": 86, "weight": 222, "shells": [2, 8, 18, 32, 18, 8]},
    "Fr": {"name": "Francium", "number": 87, "weight": 223, "shells": [2, 8, 18, 32, 18, 8, 1]},
    "Ra": {"name": "Radium", "number": 88, "weight": 226, "shells": [2, 8, 18, 32, 18, 8, 2]},
    "Ac": {"name": "Actinium", "number": 89, "weight": 227, "shells": [2, 8, 18, 32, 18, 9, 2]},
    "Th": {"name": "Thorium", "number": 90, "weight": 232.04, "shells": [2, 8, 18, 32, 18, 10, 2]},
    "Pa": {"name": "Protactinium", "number": 91, "weight": 231.04, "shells": [2, 8, 18, 32, 20, 9, 2]},
    "U":  {"name": "Uranium", "number": 92, "weight": 238.03, "shells": [2, 8, 18, 32, 21, 9, 2]},
    "Np": {"name": "Neptunium", "number": 93, "weight": 237, "shells": [2, 8, 18, 32, 22, 9, 2]},
    "Pu": {"name": "Plutonium", "number": 94, "weight": 244, "shells": [2, 8, 18, 32, 24, 8, 2]},
    "Am": {"name": "Americium", "number": 95, "weight": 243, "shells": [2, 8, 18, 32, 25, 8, 2]},
    "Cm": {"name": "Curium", "number": 96, "weight": 247, "shells": [2, 8, 18, 32, 25, 9, 2]},
    "Bk": {"name": "Berkelium", "number": 97, "weight": 247, "shells": [2, 8, 18, 32, 27, 8, 2]},
    "Cf": {"name": "Californium", "number": 98, "weight": 251, "shells": [2, 8, 18, 32, 28, 8, 2]},
    "Es": {"name": "Einsteinium", "number": 99, "weight": 252, "shells": [2, 8, 18, 32, 29, 8, 2]},
    "Fm": {"name": "Fermium", "number": 100, "weight": 257, "shells": [2, 8, 18, 32, 30, 8, 2]},
    "Md": {"name": "Mendelevium", "number": 101, "weight": 258, "shells": [2, 8, 18, 32, 31, 8, 2]},
    "No": {"name": "Nobelium", "number": 102, "weight": 259, "shells": [2, 8, 18, 32, 32, 8, 2]},
    "Lr": {"name": "Lawrencium", "number": 103, "weight": 266, "shells": [2, 8, 18, 32, 32, 8, 3]},
    "Rf": {"name": "Rutherfordium", "number": 104, "weight": 267, "shells": [2, 8, 18, 32, 32, 10, 2]},
    "Db": {"name": "Dubnium", "number": 105, "weight": 268, "shells": [2, 8, 18, 32, 32, 11, 2]},
    "Sg": {"name": "Seaborgium", "number": 106, "weight": 269, "shells": [2, 8, 18, 32, 32, 12, 2]},
    "Bh": {"name": "Bohrium", "number": 107, "weight": 270, "shells": [2, 8, 18, 32, 32, 13, 2]},
    "Hs": {"name": "Hassium", "number": 108, "weight": 277, "shells": [2, 8, 18, 32, 32, 14, 2]},
    "Mt": {"name": "Meitnerium", "number": 109, "weight": 278, "shells": [2, 8, 18, 32, 32, 15, 2]},
    "Ds": {"name": "Darmstadtium", "number": 110, "weight": 281, "shells": [2, 8, 18, 32, 32, 17, 1]},
    "Rg": {"name": "Roentgenium", "number": 111, "weight": 282, "shells": [2, 8, 18, 32, 32, 18, 1]},
    "Cn": {"name": "Copernicium", "number": 112, "weight": 285, "shells": [2, 8, 18, 32, 32, 18, 2]},
    "Nh": {"name": "Nihonium", "number": 113, "weight": 286, "shells": [2, 8, 18, 32, 32, 18, 3]},
    "Fl": {"name": "Flerovium", "number": 114, "weight": 289, "shells": [2, 8, 18, 32, 32, 18, 4]},
    "Mc": {"name": "Moscovium", "number": 115, "weight": 290, "shells": [2, 8, 18, 32, 32, 18, 5]},
    "Lv": {"name": "Livermorium", "number": 116, "weight": 293, "shells": [2, 8, 18, 32, 32, 18, 6]},
    "Ts": {"name": "Tennessine", "number": 117, "weight": 294, "shells": [2, 8, 18, 32, 32, 18, 7]},
    "Og": {"name": "Oganesson", "number": 118, "weight": 294, "shells": [2, 8, 18, 32, 32, 18, 8]}
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

def get_element():
    element = input("Enter symbol or name \n>>> ").strip()

    # creates a temporary storage for the element or symbol
    found_key = None

    # checks if symbol is in the dictionary
    if element in periodic_elements:
        found_key = element

    # if it doesn't match any symbol then searches if the element name is in the dictionary
    else:
        for symbol, data in periodic_elements.items():
            if data['name'].lower() == element.lower():  # Case-insensitive check
                found_key = symbol
                break

    # displays the element
    if found_key:
        element_data = periodic_elements[found_key]
        slow_type(f"Name: {element_data['name']}\n")
        slow_type(f"Symbol: {found_key}\n")
        slow_type(f"Energy Levels: {element_data['shells']}\n")
        slow_type(f"Valence Electrons: {element_data['shells'][-1]}\n")
    else:
        slow_type("Element not found.\n")

slow_type("Periodic Table [for a list of commands type help]\n")

while True:

    command = input(">>>")
    if command == "p table":
        periodic_series()
        periodic_table()

    elif command == "help":
        slow_type("Okay Here's the list of commands.\n help\n")
        print("help\np table\np element\np series\np period\nexit\n")

    elif command == "exit":
        break

    elif command == "p element":
        get_element()

    elif command == 'p series':
        periodic_series()
        slow_type("Would you like to know more about the series? (y/n)\n")
        a = input(">>>")
        a.lower()

        if a == "y":

            print(f"In the context of the periodic table a {"\33[92m" + 'reactive non-metals' + "\33[0m"} is a chemical element that \nmostly lacks distinctive metallic properties. They range from colorless gases like\n hydrogen to shiny crystals like iodine. Physically, they are usually lighter\n (less dense) than elements that form metals and are often poor conductors of heat and\n electricity. Chemically, {"\33[92m" + 'reactive non-metals' + "\33[0m"} have relatively high electronegativity or\n usually attract electrons in a chemical bond with another element, and\n their oxides tend to be acidic. https://en.wikipedia.org/wiki/Nonmetal\n\n")

            print(f"The {"\33[35m" + 'noble gases' + "\33[0m"}' inertness, or tendency not to react with other chemical substances, results\n from their electron configuration: their outer shell of valence electrons is\n 'full', giving them little tendency to participate in chemical reactions. Only\n a few hundred noble gas compounds are known to exist. For the same reason, {"\33[35m" + 'noble gas' + "\33[0m"}\n atoms are small, and the only intermolecular force between them is the very weak London dispersion force\n, so their boiling points are all cryogenic, below 165 K (−108 °C; −163 °F). https://en.wikipedia.org/wiki/Noble_gas\n\n")

            print(f"{"\33[31m" + 'Alkali metals' + "\33[0m"} are the chemical elements in periodic table group 1, other than hydrogen.\nThe term group 1 element can be used to include hydrogen. They are silver-coloured\nwhen pure, soft and have only one valence electron. They like to make reactions\nin which they give up this single electron and then have a charge of +1. They react\nstrongly with water and because of this, they have to be stored in oil. {"\33[31m" + 'Alkali metals' + "\33[0m"}\nare the first group in the periodic table. They are never found in nature\nuncombined because they are unstable and they react fast to other elements. They\nbond well with all elements except the noble gases. When they are in air,\nthey quickly turn black. For more information, see https://en.wikipedia.org/wiki/Alkali_metal\n\n")

            print(f"The informal chemical symbol Ln is used in general discussions of {'\33[47m' + 'lanthanide' + "\33[0m"} chemistry to \nrefer to any {'\33[47m' + 'lanthanide' + "\33[0m"}.[5] All but one of the \n{'\33[47m' + 'Lanthanide' + "\33[0m"} are f-block elements, corresponding to the filling \nof the 4f electron shell. Lutetium is a d-block element (thus also a transition \nmetal),[6][7] and on this basis its inclusion has been questioned; however, like its congeners scandium and yttrium \nin group 3, it behaves similarly to the other 14. The term rare-earth \nelement or rare-earth metal is often used to include the stable group 3 elements Sc, Y, and Lu in addition to the 4f elements.[8] All {'\33[47m' + 'lanthanide' + "\33[0m"} elements form trivalent cations, Ln3+, whose chemistry is largely determined \nby the ionic radius, which decreases steadily from lanthanum (La) to lutetium (Lu). \n https://en.wikipedia.org/wiki/Lanthanide\n\n")

            print(f"{'\33[45m' + 'Actinoids' + "\33[0m"} (or actinides) area series of 15 radioactive metallic elements in the periodic \ntable, from actinium (Ac, atomic number 89) to lawrencium (Lr, 103), defined by the \nfilling of their 5f electron shells, forming the second row of the f-block \nelements, and known for their radioactivity and variable oxidation states, including \nimportant elements like uranium and plutonium. https://en.wikipedia.org/wiki/Actinide\n\n")

            print(f"In chemistry, a transition metal (or transition element) is a chemical element in the d-block of the periodic table \n(groups 3 to 12), though the elements of group 12 (and less often group 3) are \nsometimes excluded. The lanthanide and actinide elements (the f-block) are called \ninner {'\33[90m' + 'transition metals' + "\33[0m"} and are sometimes considered \nto be transition metals as well. Since they are metals, they are lustrous and have good electrical and thermal \nconductivity. Most (with the exception of group 11 and group 12) are hard and \nstrong, and have high melting and boiling temperatures. They form compounds in any of two or more different oxidation states and bind to a variety of ligands \nto form coordination complexes that are often coloured. They form many useful alloys and \nare often employed as catalysts in elemental form or in compounds such as coordination complexes and oxides. Most are \nstrongly paramagnetic because of their unpaired d electrons, as are many of their compounds. All of the \nelements that are ferromagnetic near room temperature are transition metals (iron, cobalt and nickel) \nor inner transition metals (gadolinium). https://en.wikipedia.org/wiki/Transition_metal\n\n")

            print(f"The metallic elements in the periodic table located between the transition metals to their left and the chemically weak \nnonmetallic metalloids to their right have received many names in the literature, \nsuch as {'\33[33m' + 'post-transition metals' + "\33[0m"}, poor metals, other \nmetals, p-block metals and chemically weak metals. The most common name, \n{'\33[33m' + 'post-transition metals' + "\33[0m"}, is generally used in this article.Physically, these metals are soft \n(or brittle), have poor mechanical strength, and usually have melting points \nlower than those of the transition metals. Being close to the metal-nonmetal border, their crystalline structures tend to show covalent or directional \nbonding effects, having generally greater complexity or fewer nearest neighbours than other metallic \nelements. Chemically, they are characterised—to varying degrees—by covalent bonding tendencies, acid-base amphoterism \nand the formation of anionic species such as aluminates, stannates, and bismuthates (in the case \nof aluminium, tin, and bismuth, respectively). They can also form Zintl phases (half-metallic compounds \nformed between highly electropositive metals and moderately \n electronegative metals or metalloids). https://en.wikipedia.org/wiki/Post-transition_metal\n\n")

            print(f"A {'\33[34m' + 'metalloids' + "\33[0m"} is a chemical element which has a preponderance of properties in between, or that \nare a mixture of, those of metals and nonmetals. The word metalloid comes \nfrom the Latin metallum ('metal') and the Greek oeides ('resembling in form or appearance'). \nThere is no standard definition of a \n{'\33[34m' + 'metalloids' + "\33[0m"} and no complete agreement on which elements are metalloids. Despite the lack of specificity, the term remains \nin use in the literature. https://en.wikipedia.org/wiki/Metalloid\n\n")

            print(f"Together with helium, these elements have in common an outer s orbital which is full , this orbital contains its full \ncomplement of two electrons, which the {'\33[36m' + 'alkaline earth metals' + "\33[0m"} readily lose to form \ncations with charge +2, and an oxidation state of +2. \nHelium is grouped with the noble gases and not \nwith the alkaline earth metals, but it is theorized to have some similarities to beryllium when forced into bonding and has sometimes been suggested \nto belong to group 2. https://en.wikipedia.org/wiki/Alkaline_earth_metal\n\n")

    elif command == "p period":
        slow_type("A period on the periodic table is a horizontal row, where elements share the same number of electron shells (energy levels); as you move from left to right across a period, each element has one more proton, leading to gradual changes in properties, with the next period starting a new, higher electron shell https://en.wikipedia.org/wiki/Period_(periodic_table)")

    elif command != "help" "p table" "p element" "p series" "p period" "exit":
        slow_type("Command error. Please try again. ")

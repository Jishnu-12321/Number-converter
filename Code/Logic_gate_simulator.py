import time
valid_1 = False
while valid_1 == False:
    gate_1 = int(input("Is input 1 on (1) or off (0)"))
    time.sleep(2)
    if gate_1 > 1 and gate_1 < 0:
        print("Please enter a NUMBER which is either 1 or 0, representing the switch on or off respectively")
        valid_1 = False
    else:
        print("Valid. Processing...")
        time.sleep(1)
        valid_1 = True
        break

valid_2 = False
while valid_2 == False:
    gate_2 = int(input("Is input 2 on (1) or off (0)"))
    time.sleep(2)
    if gate_2 > 1 or gate_2 < 0:
        print("Please enter a NUMBER which is either 1 or 0, representing the switch on or off respectively")
        valid_2 = False
    else:
        print("Valid. Processing...")
        time.sleep(1)
        valid_2 = True
        break

gate_valid = False
while gate_valid == False:
    logic_gate = input("Which logic gate do you want to apply to the variables (AND, OR, XOR, NAND, NOR, XNOR).")
    time.sleep(1)
    print("processing...")
    list_1 = ["AND", "OR", "XOR", "NAND", "NOR", "XNOR"]
    if logic_gate not in list_1:
        print("Not a valid logic gate, sorry. Try again")
        gate_valid = False
    else:
        print("Valid. Processing...")
        time.sleep(1)
        gate_valid = True
        break

if gate_1 == 0:
    switch_1 = "0 (off switch of gate 1)"
else:
    switch_1 = "1 (on switch of gate 1)"
if gate_2 == 0:
    switch_2 = "0 (off switch of gate 2)"
else:
    switch_2 = "1 (on switch of gate 2)"


if logic_gate == "AND":
    if gate_1 == 1 and gate_2 == 1:
        print(f"{switch_1} {logic_gate} {switch_2} is 1")
    else:
        print(f"{switch_1} {logic_gate} {switch_2} is 0")
elif logic_gate == "OR":
    if gate_1 == 1 or gate_2 == 1:
        print(f"{switch_1} {logic_gate} {switch_2} is 1")
    else:
        print(f"{switch_1} {logic_gate} {switch_2} is 0")
elif logic_gate == "XOR":
    if (gate_1 == 1 and gate_2 == 0) or (gate_1 == 0 and gate_2 == 1):
        print(f"{switch_1} {logic_gate} {switch_2} is 1")
    else:
        print(f"{switch_1} {logic_gate} {switch_2} is 0")
elif logic_gate == "NAND":
    if gate_1 == 1 and gate_2 == 1:
        print(f"{switch_1} {logic_gate} {switch_2} is 0")
    else:
        print(f"{switch_1} {logic_gate} {switch_2} is 1")
elif logic_gate == "NOR":
    if gate_1 == 0 and gate_2 == 0:
        print(f"{switch_1} {logic_gate} {switch_2} is 1")
    else:
        print(f"{switch_1} {logic_gate} {switch_2} is 0")
elif logic_gate == "XNOR":
    if gate_1 == gate_2:
        print(f"{switch_1} {logic_gate} {switch_2} is 1")
    else:
        print(f"{switch_1} {logic_gate} {switch_2} is 0")




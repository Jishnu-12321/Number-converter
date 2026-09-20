import math
import time
import random

try:
    number_type1 = int(input(""" What number type do you want to translate from? 
        1 - Binary
        2 - Denary
        3 - Hexadecimal"""))

except ValueError:
    print("Please enter a number from 1, 2 or 3")


else:
    if number_type1 == 1:
        while True:
            try:
                binary = input("Please input what binary number you would like to translate to: ")
                numbers = list(binary)
                
                if len(numbers) == 0:
                    print("Error: Input cannot be empty. Please try again.\n")
                    continue
                    
                is_binary = True
                for digit in numbers:
                    if digit != '0' and digit != '1':
                        is_binary = False
                        break

                if is_binary:
                    print("processing...")
                    time.sleep(3)
                    print("Valid binary number")
                    print(numbers)

                    break
                else:
                    print("Error: Please enter a binary number containing ONLY 0s and 1s.\n")
                    
            except ValueError:
                print("Please enter a binary number\n")

        numbers.reverse() 

        denary = 0

        for i in range(len(numbers)):
            multiplier = 2 ** i
            
            digit = int(numbers[i])
            
            denary += digit * multiplier
        print("translating to denary...")
        time.sleep(3)
        print(f"The binary number - {binary}, is {denary} in denary form")
        

        while len(binary) % 4 != 0:
            binary = "0" + binary
        
        hex_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        hexa = ""
        for i in range(0, len(binary), 4):
            nibble = binary[i:i+4]
            
            nibble_list = list(nibble)
            nibble_list.reverse()
            
            chunk_denary_total = 0
            for j in range(len(nibble_list)):
                multiplier = 2 ** j
                digit = int(nibble_list[j])
                chunk_denary_total += digit * multiplier
                
            hexa += hex_chars[chunk_denary_total]

        print("translating to hexadecimal...")
        time.sleep(3)
        print(f"The binary value - {binary}, is {hexa} in hexadecimal form.")

        print(f"{binary} is {denary} in denary and {hexa} in hexadecimal")

    if number_type1 == 2:
        while True:
            try:
                denary = input("Please input what denary number you would like to translate: ")
                
                if len(denary) == 0:
                    print("Error: Input cannot be empty. Please try again.\n")
                    continue
                    
                denary = int(denary)
                if denary < 0:
                    print("Error: Please enter a positive integer.\n")
                    continue    
                break
                
            except ValueError:
                print("Error: Please enter a valid whole number (no letters or decimals).\n")
        print("processing...")
        time.sleep(2)
        print("Valid denary form.")
        num_for_binary = denary

        binary_remainders = []
        
        if num_for_binary == 0:
            binary_remainders.append(0)
            
        while num_for_binary > 0:
            remainder = num_for_binary % 2
            binary_remainders.append(str(remainder))
            num_for_binary = num_for_binary // 2
        
        binary_remainders.reverse()
        binary = "".join(binary_remainders)
        
        time.sleep(2)
        print("translating to binary...")
 
        while len(binary) % 4 != 0:
            binary = "0" + binary
 
        time.sleep(random.randint(3, 5))
        print(f"{denary} is {binary} in Binary form.")


        num_for_hex = denary
        
        hex_remainders = []
        hex_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        
        if num_for_hex == 0:
            hex_remainders.append("0")
            
        while num_for_hex > 0:
            remainder = num_for_hex % 16
            hex_char = hex_chars[remainder]
            hex_remainders.append(hex_char)
            num_for_hex = num_for_hex // 16
        
        hex_remainders.reverse()
        hexa = "".join(hex_remainders)
        
        time.sleep(2)
        print("translating to hexadecimal...")
        
        time.sleep(3)
        print(f"{denary} is {hexa} in hexadecimal form.")

        print(f"{denary} is {binary} in binary and {hexa} in hexadecimal.")

    if number_type1 == 3:
        hex_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        while True:
            hex_input = input("Please input the Hexadecimal number you would like to translate: ").strip().upper()
            numbers = list(hex_input)
            if len(numbers) == 0:
                print("Error: Input cannot be empty. Please try again.\n")
                continue

            is_hex = True
            for char in numbers:
                if char not in hex_chars:
                    is_hex = False
                    break
                    
            if is_hex:
                print("Valid Hexadecimal number accepted!")
                break
            else:
                print("Error: Please enter a valid Hexadecimal string (0-9, A-F).\n")
        time.sleep(2)

        print("processing...")
        time.sleep(2)
        
        print("Correct hexadecimal form.")
        time.sleep(2)
        
        print("translating to denary...")
        time.sleep(3)

        numbers.reverse()
        denary = 0

        for i in range(len(numbers)):
            char = numbers[i]
            value = hex_chars.index(char) 
            multiplier = 16 ** i
            denary += value * multiplier
        
        print(f"{hex_input} is {denary} in denary form.")

        num_for_binary = denary
        binary_remainders = []

        if num_for_binary == 0:
            binary_remainders.append("0")

        while num_for_binary > 0:
            binary_remainders.append(str(num_for_binary % 2))
            num_for_binary = num_for_binary // 2
        
        binary_remainders.reverse()
        binary = "".join(binary_remainders)

        while len(binary) % 4 != 0:
            binary = "0" + binary
        
        print("translating to binary...")
        time.sleep(2)
        print(f"{hex_input} is {binary} in binary form.")
        time.sleep(1)
        print(f"{hex_input} is {denary} in denary and {binary} in binary.")
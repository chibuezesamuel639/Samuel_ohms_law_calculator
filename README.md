# Samuel_ohms_law_calculatorOhm’s Law and Power Calculator

Course: CTE123 – Python Mini Project
Programme: ND1 Mechatronics Engineering
Institution: Yaba College of Technology (YabaTech)

##What it does##

The Ohm’s Law and Power Calculator is a menu-driven Python program that calculates voltage, current, resistance, or electrical power when the user enters two known quantities. It displays the answer with the correct unit.

The program also checks for invalid input, prevents calculations that require division by zero, and keeps a history of successful calculations during the current session.

##Electrical formulas used##

• Voltage: V = I × R
• Current: I = V ÷ R
• Resistance: R = V ÷ I
• Power: P = V × I
• Power: P = I² × R
• Power: P = V² ÷ R

The program rearranges these formulas to calculate the requested quantity from other valid pairs of known values.

##How to run it##

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

python ohms_law.py

##How to use it##

1. Run the program.
2. Select voltage, current, resistance, or power.
3. Choose the pair of electrical quantities you already know.
4. Enter the two values when prompted.
5. Read the result and its unit.
6. Select View calculation history to review results from the current session, or select Quit to exit.

##Sample output##

===== OHM'S LAW AND POWER CALCULATOR =====
1. Calculate voltage (V)
2. Calculate current (I)
3. Calculate resistance (R)
4. Calculate power (P)
5. View calculation history
6. Quit
Choose an option (1-6): 1

To calculate voltage, choose the two values you know:
1. Current and Resistance
2. Power and Current
3. Power and Resistance
Choose a pair (1-3): 1
Enter current (A): 2
Enter resistance (ohms): 5

Result: Voltage = 10.0000 V
‘’’
My own twist

I added a calculation history feature. The program saves each successful result while it is running. The user can select option 5 to review results from that session.

Input validation and error handling

• The program asks again if the user enters text instead of a number.
• Negative values and non-finite numbers are rejected.
• Invalid menu and pair selections produce helpful messages.
• Calculations that require division by zero are stopped with an explanatory message.

What I learned

I practised using Python functions, while loops, if/elif/else statements, dictionaries, lists, and float() for numeric input. I also practised validating user input, handling calculation errors, and applying electrical engineering formulas in a Python program.

Author

[Your Full Name]
ND1 Mechatronics Engineering, Yaba College of Technology (YabaTech)

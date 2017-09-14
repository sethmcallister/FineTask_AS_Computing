# This will check if the inputed data type can be casted to a float
def notValidNumber(number):
    result = True;
    try:
        float(number);
        result = False;
    except ValueError:
        result = True;
    return result;


def askForSpeed():
    try:
        return input("Please enter the user's speed.");
    except KeyboardInterrupt:
        quit();

speedSTR = askForSpeed();
while(notValidNumber(speedSTR)):
    print("Please input a valid number; eg. 1.1, or 1");
    speedSTR = askForSpeed();

speed = float(speedSTR);
fine = 0;
if speed >= 41 and speed < 60:
    fine = 100;
elif speed >= 60 and speed < 100:
    fine = 250;
elif speed >= 100:
    fine = 500;

if fine == 0:
    print("This user should not be fined.");
else:
    print("The user should be fined £", fine);

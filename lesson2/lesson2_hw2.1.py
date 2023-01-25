"""In a particular jurisdiction, older license plates consist of three uppercase letters followed by three numbers.
When all the license plates following that pattern had been used, the format was changed to four numbers followed by
three uppercase letters.
Write a program that begins by reading a string of characters from the user.
Then your program should display a message indicating whether the characters are valid for an older style license plate
or a newer style license plate. Your program should display an appropriate message if the string entered by the user
is not valid for either style of license plate."""

car_plate = input('Car plate: ')
result = None

if car_plate[0:2].isalpha() and car_plate[3:5].isdigit():
    result = 'old style'
elif car_plate[0:3].isdigit() and car_plate[4:6].isalpha():
    result = 'new style'

if result:
    print(f'The car plate number refers to {result}.')
else:
    print('The car plate number is invalid. Try again.')

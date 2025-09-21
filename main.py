from pyscript import document, display

def adding_numbers(e): #e for event handling
    num1 = float(document.getElementById("input1").value) #Accessing the value given by the user on input1 id
    num2 = float(document.getElementById("input2").value) #Accessing the value given by the user on input2 id
    average = (num1 + num2) / 2 #getting average

    display(average, target = "output1")
    if (average < 75): #checking if average is less than 75
        display ("No, Failed.", target = "result")
    else:
        display ("Yes, Passed.", target = "result")

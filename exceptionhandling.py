try:
    num=int(input())
    print(10/num)
# except ZeroDivisionError:
#     print("The integer cannot be divided by 0")
# except ValueError:
#     print("Given input not belongs to the integer datatype")
except Exception as e:  # it will the all type of error
    print("Error Occured",e)
else:  # executes when the try block has no error 
    print("Successfully executed")
finally:  # executes at the end of the program if the code has error or not
    print("Execution completed")
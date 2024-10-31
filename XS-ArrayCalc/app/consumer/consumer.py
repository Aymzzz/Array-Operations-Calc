from zeep import Client

ArrayOperations = Client("app/src/main/resources/ArrayOpsService.wsdl").service #stub client


ArrayIn = [1,4,3,7,0,6,8]
ArrayIn2 = [1,2,3,4,5,6,9]

sorted_array = ArrayOperations.sortArray(ArrayIn)
print("The sorted array is: ", sorted_array)

max_val = ArrayOperations.maxArray(ArrayIn)
print("The max value is: ", max_val)

min_val = ArrayOperations.minArray(ArrayIn)
print("The min value is: ", min_val)

sum_result = ArrayOperations.sumArrays(ArrayIn, ArrayIn2)
print("The summed Array is: ", sum_result)

mul_result = ArrayOperations.multiplyArrays(ArrayIn, ArrayIn2)
print("The product Array is: ", mul_result)


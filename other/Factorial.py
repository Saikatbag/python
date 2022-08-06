def FirstFactorial(num):

  # code goes here
  result = 1
  if num >= 1:
    result = num* FirstFactorial(num - 1)
  return result

# keep this function call here 
print(FirstFactorial(input()))
# Function Definitions
def calculateFine(speedLimit, speed):
    
     diff = speed - speedLimit 

     if speed <= speedLimit or diff < 5:
        return 0
     elif diff >= 5 and diff < 15:
        return 10
     elif diff >= 15 and diff < 25:
        return 20
     elif diff >= 25 and diff < 40:
        return 40
     else: 
        return 60

# Start of Program

try:
  speedLimitVar = int(input("enter speed limit: "))
  speedVar = int(input("enter speed: "))

  fineVar = calculateFine(speedLimitVar, speedVar)
  print(f"fine: ${fineVar}")

except ValueError:
   print("Please enter a valid integer.")

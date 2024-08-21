engine_indicator_light = "red blinking"
space_suits_on = True
shuttle_cabin_ready = True
<<<<<<< HEAD
crew_Status = space_suits_on and shuttle_cabin_ready
computerStatusCode = 200
shuttleSpeed = 15000
=======
crew_status = space_suits_on and shuttle_cabin_ready
computer_status_code = 200
shuttle_speed = 15000
>>>>>>> 4c49cc65fae8b51d2ac955a031b7ede3e558db82

# 3) Write conditional expressions to satisfy the following safety rules:

# a) If crew_status is true, print "Crew Ready" else print "Crew Not Ready".
if crew_Status == True:
    print("Crew Ready")
else:
    print("Crew Not Ready")


# b) If computer_status_code is 200, print "Please stand by. Computer is rebooting." Else if computer_status_code is 400, print "Success! Computer online." Else print "ALERT: Computer offline!"
if computerStatusCode == 200:
    print("Please stand by. Computer is rebooting.")
elif computerStatusCode == 400:
    print("Success! Computer online.")
else:
    print("ALERT! Computer offline.")

# c) If shuttle_speed is > 17,500, print "ALERT: Escape velocity reached!" Else if shuttle_speed is < 8000, print "ALERT: Cannot maintain orbit!" Else print "Stable speed".
if shuttleSpeed > 17500:
    print("ALERT: Escape velocity reached!")
elif shuttleSpeed < 8000:
    print("ALERT: Cannot maintain orbit!")
else:
    print("Stable speeds")

# 4) PREDICT: Do the code blocks shown in the Section D produce the same result?

<<<<<<< HEAD
print("Yes")
=======
# print("Yes" or "No")
>>>>>>> 4c49cc65fae8b51d2ac955a031b7ede3e558db82

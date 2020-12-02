cake = float(input("Enter the pieces of cake you have eaten:"))
kilometers= float(input("Enter the Kilometers you have run:"))
kilometers_ran = kilometers*100
cake_jog= ((225*cake)-kilometers_ran)
print ("This is how many calories you have lost:" + str(cake_jog))

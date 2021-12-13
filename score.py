score = input("Enter Score between 0.0 and 1.0: ")

try:
    fscore = float(score)
    
except:
    print("Enter a number between 0.0 and 1.0")
    quit()
    
if fscore > 1.0:
    print("Enter a number between 0.0 and 1.0")
elif fscore >= 0.9:
	print("A")
elif fscore >= 0.8:
	print("B")
elif fscore >= 0.7:
   	print("C")
elif fscore >= 0.6:
   	print("D")
elif fscore < 0.6:
   	print("F")

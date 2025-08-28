questions = ("How many elements are in the periodic table?: ",
              "Which animal lays the largest egg?: ",
              "Who is the prime minister of India?: ")
options = (("A.116", "B.117" , "C.118" , "D.119"),
           ("A.Whale" , "B.Elephant" , "C.Ostrich" , "D.Pig"),
            ("A.Narendra Modi", "B.Rahul Gandhi" , "C.Nethaji" , "D.Ram Mohan Singh"))
i = 0
score = 0
guesses=[]
answers = ("C","C","A")
for question in questions:
    print(question)
    for option in options[i]:
        print(option)
    guess = input("Enter the answer:").upper()    
    guesses.append(guess)
    if guess == answers[i]:
        print("Correct answer!")
        score += 1
    else:
        print("Wrong answer!")
        print(f"The correct answer is {answers[i]}")
    i += 1
percent = (score/3)*100
print(f"Your percentage is {percent:.1f}%")
print("Results")
for guess in guesses:
    print(guess,end = " ")
print()
for answer in answers:
    print(answer, end = " ")
print()

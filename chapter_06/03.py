p1="Mak a lot of money"
p2="buy now"
p3="subscribe this"
p4="click here"

massage=input("Enter your massage:")
if((p1 in massage) or (p2 in massage) or (p3 in massage) or (p4 in massage)):
    print("Spam Massage........")
else:
    print("This massage is not spam.........")    
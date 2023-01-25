nominee1 = input("Enter the name of 1st political party:")
nominee2 = input("Enter the name of 2nd political party:")
nominee3 = input("Enter the name of 3rd political party:")

nm1_votes = 0
nm2_votes = 0
nm3_votes = 0

voter_id = [1,2,3,4,5]

no_of_voter = len(voter_id)

while True:
    if voter_id == []:
        print("Voting session is over")
        
        print(nominee1,(nm1_votes/no_of_voter)*100)
        print(nominee2,(nm2_votes/no_of_voter)*100)
        print(nominee3,(nm3_votes/no_of_voter)*100)
        break
    
    voter = int(input("Enter your voter id :"))
    if voter in voter_id:
        print("Yor are a voter")
        voter_id.remove(voter)
        print("------------------------------------------")
        print("To give vote to " ,nominee1, "Press 1" )
        print("To give vote to " ,nominee2, "Press 2" )
        print("To give vote to " ,nominee3, "Press 3" )
        print("------------------------------------------")
        vote = int(input('Enter your precious vote:'))
        if vote == 1:
            nm1_votes += 1
            print(nominee1,"thanks you to give your important vote to our party")
        elif vote == 2:
            nm2_votes += 1
            print(nominee2,"thanks you to give your important vote to our party")
        elif vote == 2:
            nm3_votes += 1
            print(nominee3,"thanks you to give your important vote to our party")
        elif vote > 2 :
            print("Check your press key")       
        else:
            print("You are not a voter OR You have already voted")
        





def match_status(team, match_won):
    if (match_won):
        print(f"{team} won the match")
    else:
        print(f"{team} lost the match")

match_status("SRH", True)
match_status("CSK", False)
match_status("RCB", True)
match_status("MI", False)

def login_status(email,password):
    if email and password==True:
        print("Login sucessfully")
    else:
        print("Login is Failed")
login_status(True,True)
login_status(False,True)
login_status(True,False)
login_status(False,False)
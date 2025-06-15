def stud(name, age, gender, qualification):
    print("name:", name)
    print("age:", age)
    print("gender:", gender)
    print("qualification:", qualification)

stud("alice", 21, "female", "b.sc")


def food(*foods):
    print(*foods)

food("iddly", "dosa", "puri")


def bus(passengername, fromplace, toplace, buspartner="ABHIBUS"):
    return (f"hello {passengername}, greetings from {buspartner} "
            f"your journey {fromplace} to {toplace} is confirmed. HAPPY JRNY")

print(bus("john", "hyd", "vijayawada"))
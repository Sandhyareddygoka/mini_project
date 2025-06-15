def job(language):
    if(language == "frontend" and language == "backend" and language == "backend"):
        return "full stack developer"
    elif(language == "frontend" or language == "frontend" or language == "frontend"):
        return "front end developer"
    elif(language == "backend" or language == "backend" or language == "backend"):
        return "backend developer"
    elif(language == "database" or language == "database" or language == "database"):
        return "database developer"
    else:
        return "go and learn asap from institute"

res = input()
print(job(res))
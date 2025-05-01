DB = {}
id = 100
def register(name, email, password):
    global id
    if not email.endswith("@gmail.com"):
        return "Invalid email"
    
    if not len(password) >= 8:
        return "Password length must be 8 characters long"
    
    if not email in DB:
        id = id+1
        token = str(id)
        DB[token] = {"name" : name, "id":id,"email":email, "password":password, "status" : None}
        return "Registration successfull"
    return "Email already exists"



def issue_uniform(token):
    if not token in DB:
        return "Student not registered"
    if DB[token]["status"] == None:
        DB[token]["status"] = "Distributed"
        return f"Uniform issued for student ID : {DB[token]}"
    return f"Uniform already issued for student ID : {DB[token]}"

def view_issue_record():
    if not DB:
        return "Record is empty"
    return DB


print(register("Gayathri", "gayathri@gmail.com", "12345678"))
print(register("Ancy", "Ancy@gmail.com", "87654321"))
print(register("Gayathri", "gayathri", "12345678"))
print(register("Gayathri", "gayathri@gmail.com", "123458"))

print(issue_uniform("101"))
print(issue_uniform("102"))

print(view_issue_record())
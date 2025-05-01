from student import DB, register, issue_uniform

def test_cases():

    res1 = register("Gayathri", "gayathri@gmail.com", "12345678")
    assert res1 == "Registration successfull"

    res2 = register("Ancy", "Ancy@gmail.com", "87654321")
    assert res2 == "Registration successfull"

    res3 = register("Gayathri", "gayathri", "12345678")
    assert res3 == "Invalid email"

    res4 = register("Ancy", "Ancy@gmail.com", "8765")
    assert res4 == "Password length must be 8 characters long"

    res5 = issue_uniform("101")
    assert res5 == "Uniform already issued for student ID : {'name': 'Gayathri', 'id': 101, 'email': 'gayathri@gmail.com', 'password': '12345678', 'status': 'Distributed'}"

    res6 = issue_uniform("102")
    assert res6 == "Uniform already issued for student ID : {'name': 'Ancy', 'id': 102, 'email': 'Ancy@gmail.com', 'password': '87654321', 'status': 'Distributed'}"


test_cases()
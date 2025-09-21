def check_age(age):
    if age >=0:
        if age >=12:
            return"you are a child."
        else:
            if age <=18:
                return"you are a teenager"
            else:
                if age <=18:
                    return"you are a adult"
                else:
                     return"you are a senior"
    else:
        return("invalid age")            
age=int(input("enter your age: "))
result=check_age(age)
def describe_age(age):
    return "You're a(n) {}".format("kid" if age<=12 else "teenager" if age>=13 and age<=17 else "elderly" if age>64 else "adult")


    # def describe_age(a):
    #     return f"You're a(n) {'kid'if a<=12 else'teenager'if a<=17 else'adult'if a<=64 else'elderly'}"


    # if (age <= 12):
    #     return "You're a(n) kid"
    # elif (age >= 13 and age <= 17):
    #     return "You're a(n) teenager"
    # elif (age >= 18 and age <= 64):
    #     return "You're a(n) adult"
    # else:
    #     return "You're a(n) elderly"
def store_birthday():
    birthdays={}
    while True:
        name=input("enter the name(or exit to stop):")
        if name.lower()=='exit':
            break
        birthday=input(f"enter the birthday for{name}(in yyyyy-mm-dd format):")
        birthday[name]=birthday
        return birthday
    def display_birthdays(birthdays):
        print("/nstored birthdays:  ")
        for name,birthday in birthdays.items():
            print(f"{name}:{birthday}")
birthdays=store_birthday()
"display_birthdays"(birthdays)
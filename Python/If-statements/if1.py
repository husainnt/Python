#used as a check/condition before/during a process, syntax-> if:, else:
cars=['bmw','audi','pagani','mercedes']
for c in cars:
    if c=='bmw':
        print(c.upper())
    else:
        print(c.title())

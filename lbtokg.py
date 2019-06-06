def lbs_kgs(lbs):
    kgs=lbs*0.454
    return kgs
input = (input("Enter a list element separated by space "))
list  = input.split()
for item in list:
    print(round(lbs_kgs(float(item))))





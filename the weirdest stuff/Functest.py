def case(j:int) -> int:
    return None

i = int(input("test: "))
j = i+1
match i:
    case 2: print("3")
    case(j): print("fuck")


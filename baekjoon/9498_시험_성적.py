def sol(n):
    if n >= 90:
        return "A"
    if n >= 80:
        return "B"
    if n >= 70:
        return "C"
    if n >= 60:
        return "D"
    else:
        return "F"

n = int(input())
print(sol(n))
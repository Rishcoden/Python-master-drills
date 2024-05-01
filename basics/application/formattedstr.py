s = input()

hrs, mins, sec = map(int, s[:8].split(":"))
d = s[-2:]

if d == "AM" and hrs == 12:
    hrs = 0
elif d == "PM" and hrs != 12:
    hrs = hrs + 12

result = f"{hrs:02d}:{mins:02d}:{sec:02d}"

print(result)

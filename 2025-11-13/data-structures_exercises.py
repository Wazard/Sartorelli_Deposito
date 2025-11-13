def words_to_int(s):
    ones = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,"five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    teens = {"ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,"fourteen": 14, "fifteen": 15, "sixteen": 16,"seventeen": 17, "eighteen": 18, "nineteen": 19}
    tens = {"twenty": 20, "thirty": 30, "forty": 40,"fifty": 50, "sixty": 60, "seventy": 70,"eighty": 80, "ninety": 90}
    multipliers = {"hundred": 100,"thousand": 1000}


    s = s.lower().replace("-", " ").replace(" and ", " ") # Normalize input
    parts = s.split()

    total = 0
    i = -1
    while i+1 < len(parts):
        i+=1
        word = parts[i]

        # limit cases
        if word in ones:
            if i+1<len(parts):
                if parts[i+1] in multipliers and not parts[i-1] in tens: # skips in case the word is a unit and not a multiplier (ex two thousand, seven hundred...)
                    total += ones[word] * multipliers[parts[i+1]]
                    i+=1
                    continue # go next in case of composite number (ex. one hundred, six thousand)

            total+=ones[word] #do i really have to comment this??
        elif word in teens:
            total += teens[word]
        elif word in tens:
            total += tens[word]
        elif word in multipliers:
            total *= multipliers[word]
        else:
            raise ValueError(f"Unsupported word: {word}")

    return total

user_input = input("Insert a number (ex. 1, two, one hundred, twelve thousand ...): ")
response = "your number is "

if user_input.isdigit(): # checking if user used a string or not
    num = int(user_input)
else:
    num = words_to_int(user_input)

if num%2 == 0: # checking if even or odd
    response += "even: "
else:
    response += "odd: "
print(response)
print(num)
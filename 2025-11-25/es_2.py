import numpy as np

# Generate arrays
arr = np.linspace(start=0, stop=10, num=50)
arr0 = np.random.random(size=50)
arr1 = arr + arr0

# Sums
sum1 = np.sum(arr1)
mask = arr1 > 5
sum1_greater_5 = np.sum(arr1[mask])

# Prepare output string
output = (
    f"OG_ARR1:\n{arr}\n"
    f"OG_ARR2:\n{arr0}\n"
    f"SUM_ARR:\n{arr1}\n"
    f"SUM_TOT: {sum1}\n"
    f"SUM_GREATER_5: {sum1_greater_5}\n"
)

print(output)

# Ask user how to save
choice = input("Do you want to overwrite (o) or append (a) to results.txt? [o/a]: ").strip().lower()

filename = "2025-11-25/results.txt"
mode = "w" if choice == "o" else "a"

# Write data
with open(filename, mode) as f:
    if mode == "a":
        f.write("\n--- New Run ---\n")
    f.write(output)

print(f"Data saved to {filename} ({'overwritten' if mode == 'w' else 'appended'}).")
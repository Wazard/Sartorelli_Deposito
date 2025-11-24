arr = [1,2,3,4,5,10,7,8,9,10]

result = list(
    map(lambda i: arr[i], filter(lambda i: arr[i] + arr[i+1] > arr[i+2], range(len(arr)-2)))
)

# range gives us a list of all indices but last 2 (len(arr)-2)
# condition: arr[i]+arr[i+1]>arr[i+2]
# then each filtered index is mapped to arr

print(result)
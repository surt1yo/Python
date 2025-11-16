#Write a function that accepts the beginning and end range of numbers, 
#and find the square values of those numbers.
#Then filter the odd and even square values and print them.
def square_values_in_range(start, end):
    even_squares = []
    odd_squares = []
    for num in range(start, end + 1):
        square = num ** 2
        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)
    return even_squares, odd_squares
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
even_squares, odd_squares = square_values_in_range(start_range, end_range)
print("Even squares:", even_squares)
print("Odd squares:", odd_squares)

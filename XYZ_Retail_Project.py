#Task 1: Sales Data Summary
Category_A = 150
Category_B = 120

#Calculating the total units sold
Category_C = Category_A + Category_B

#Calculating the difference between the categories
Category_D = Category_A - Category_B

#Calculating the ratio of units sold
Category_E = Category_A / Category_B

#Printing the results
print("Sales Summary:\nTotal Units Sold:",Category_C,
      "\nDifference Between Categories:", Category_D,
      "\nRatio of Category A to Category B:", Category_E)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Task 2: Customer Age Data
#Sample Input: Customer details
Customer_Name = "John Doe"
Customer_Age = 30

#Creating the personalized marketing message
message = "Dear " + Customer_Name + ", at " + str(Customer_Age) + ", you’re eligible for our premium loyalty program."

#Printing the message for use in email campaigns
print(message)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Task 3: Product List Management
product_prices = [50, 120, 30, 200, 90, 150, 180]
premium_product_price = 250

highest_price = max(product_prices) #Extracting Highest Price
lowest_price = min(product_prices) #Extracting Lowest Price

mid_rage_product = [price for price in product_prices if price != highest_price and price != lowest_price] #Creating a new list with the mid-range products

updated_product_prices = product_prices + [premium_product_price] #Adding premium product price

#Printing Outputs
print("Highest Price: ", highest_price)
print("Lowest Price: ", lowest_price)
print("Mid-Range Products: ", mid_rage_product)
print("Updated Product List with Premium Price: ",updated_product_prices)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Task 4: Inventory Lookup
product_info = {"product_name": "Wireless Mouse", "SKU": "WM-12345", "price": 25.99, "category": "Electronics"} #Creating a dictionary storing key information about a product
print("Product Name: ", product_info["product_name"],"           ","Product SKU: ", product_info["SKU"]) #Printing the product name and SKU when queried by a customer service representative

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Task 5: Stock Level Alert System
Stock_Level = int(input("Enter Stock Level: ")) #Taking  stock level inputs from user
Threshold = 20
#Check Stock Level against Threshold
if Stock_Level < Threshold:
    print("Reorder Now")
else: print("Stock is sufficient")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Task 6: Sales Report Formatting
products_sold = ["wireless mouse", "keyboard", "headphones", "monitor", "laptop"] #Sample input list of products sold
print("#---- Using 'for' loop ----")

#Using for loop to print each product name in uppercase
for product in products_sold:
    print(product.upper())
print("\n---- Using 'while' loop ----")
i = 0
while i < len(products_sold):
    print(products_sold[i].upper())
    i+=1

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Task 7: Area Calculation for Store Layout
#Function to calculate area of a store section.
def calculate_area(length,width):
    return length*width

#Main function to calculate and print the area of several store sections.
def main():
    #Section 1
    length1, width1 = 20, 15
    print(f"The area of section 1 is {calculate_area(length1, width1)} square meters.")
    #Section 2
    length2, width2 = 10, 8
    print(f"The area of section 2 is {calculate_area(length2, width2)} square meters.")
    #Section 3
    length3, width3 = 25, 12
    print(f"The area of section 3 is {calculate_area(length3, width3)} square meters.")
main()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Task 8: Customer Feedback Analysis
def analyze_feedback(feedback):
    #Counting vowels (both uppercase and lowercase)
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in feedback if char in vowels)
    #Reversing the Feedback
    reversed_feedback = feedback[::-1]
    #Printing the Output
    print("Customer Feedback Analysis:")
    print("Original Feedback:", feedback)
    print("Number of Vowels:", vowel_count)
    print("Reversed Feedback:", reversed_feedback)

# Sample Input from the user
feedback_message = input("Enter feedback message")
analyze_feedback(feedback_message)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Task 9: Price Filtering Tool
product_prices = [150, 85, 300, 120, 45, 200] #Sample Input
Discount_Threshold = 100
eligible_products = [price for price in product_prices if price < Discount_Threshold] #filtering out products priced below a certain threshold from the product list.

#Print the list of eligible products for a discount campaign
print("Products eligible for discount campaign: ", eligible_products)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Task 10: Daily Sales Average
daily_sales = [1200, 1500, 1100, 1800, 1700, 1600, 1400] #Sample input for Sales for the past 7 days
avg_daily_sales = sum(daily_sales) / len(daily_sales) #Calculating average sales

#Printing the average sales to help the finance team understand the weekly performance
print(f"Average Daily Sales for the Past Week: ${avg_daily_sales:.2f}")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Task 11: Customer Segmentation
customer_spendings = [200, 800, 1500, 3000, 450, 1200] #Sample input for customer spendings

#Looping through spendings and categorizing each customer
print("Customer Spending Categories:")
for i, spending in enumerate(customer_spendings, start=1):
    if spending >= 1500:
        category = "High"
    elif spending >= 500:
        category = "Medium"
    else:
        category = "Low"
    print(f"Customer {i}: Spening = ${spending} --> Category: {category}")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Task 12: Discount Calculation
# Function to calculate final price after discount
def calculated_final_price(original_price, discount_percentage):
    discount_amount = (discount_percentage/100)*original_price
    return original_price - discount_amount

#Sample input: list of products with price and discount
products = [
    {"name": "Product A", "original_price": 100, "discount_percentage": 10},
    {"name": "Product B", "original_price": 250, "discount_percentage": 20},
    {"name": "Product C", "original_price": 75, "discount_percentage": 15},
    {"name": "Product D", "original_price": 150, "discount_percentage": 5}
]
print("Final Prices After Discounts:")

# Loop through products and print final prices
for i, product in enumerate (products, start=1):
    final_price = calculated_final_price(product["original_price"], product["discount_percentage"])
    print(f"Product {i}: Original Price = ${product["original_price"]}, "
          f"Discount = {product["discount_percentage"]}%, "
          f"Final Price= ${final_price:.2f}")
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Task 13: Customer Feedback Sentiment Analysis
feedback = input("Enter customer feedback") #Taking input from the user

positive_words = ["good", "happy", "excellent", "great"]
negative_words = ["bad", "disappointed", "poor", "terrible"]

feedback_lower = feedback.lower() #Converting feedback to lowercase for consistent matching

# Check sentiment
if any(word in feedback_lower for word in positive_words):
    sentiment = "Positive"
elif any(word in feedback_lower for word in negative_words):
    sentiment = "Negative"

#Printing Output
print("Customer Feedback Sentiment:", sentiment)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Task 14: Employee Salary Increment Calculator
#Creating dictionary that stores employee names and their performance ratings.
employees = {
    "Alice": {"current_salary": 50000, "rating": "Excellent"},
    "Bob": {"current_salary": 40000, "rating": "Good"},
    "Charlie": {"current_salary": 45000, "rating": "Average"},
    "David": {"current_salary": 35000, "rating": "Poor"}
}

#Increment percentages based on performance rating
increments = {
    "Excellent": 20,
    "Good": 15,
    "Average": 10,
    "Poor": 5
}
print("Updated Salaries After Increment:")

#Loop through employees and calculate updated salary
for name, details in employees.items():
    current_salary = details["current_salary"]
    rating = details["rating"]
    increment_percentage = increments[rating]
    updated_salary = current_salary + (current_salary * increment_percentage / 100)

    print(f"{name}: Current Salary = ${current_salary}, Rating = {rating}, Updated Salary = ${updated_salary:.2f}")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Task 15: Stock Replenishment Planning
# Product stock data
products = [
    {"product_name": "Product A", "stock": 50},
    {"product_name": "Product B", "stock": 150},
    {"product_name": "Product C", "stock": 30},
    {"product_name": "Product D", "stock": 75},
    {"product_name": "Product E", "stock": 20}
]

# Stock Threshold
threshold = 40

print("Products that need replenishment:")
for product in products:
    if product["stock"] < threshold:
        print(product["product_name"])

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
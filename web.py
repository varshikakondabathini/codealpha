# Import Required Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Send Request to Website
response = requests.get(url)

# Check Website Connection
if response.status_code == 200:
    print("Website Connected Successfully!\n")
else:
    print("Failed to Connect Website")
    exit()

# Parse HTML Content
soup = BeautifulSoup(response.text, "html.parser")

# Find All Book Containers
books = soup.find_all("article", class_="product_pod")

# Empty List to Store Data
book_data = []

# Extract Data from Each Book
for book in books:

    # Extract Book Title
    title = book.h3.a["title"]

    # Extract Book Price
    price = book.find("p", class_="price_color").text

    # Clean Price Data
    price = ''.join(
        ch for ch in price
        if ch.isdigit() or ch == '.'
    )

    # Convert Price to Float
    price = float(price)

    # Extract Rating
    rating = book.find("p")["class"][1]

    # Extract Availability
    availability = book.find(
        "p",
        class_="instock availability"
    ).text.strip()

    # Extract Product Link
    link = "https://books.toscrape.com/" + book.h3.a["href"]

    # Store Data in List
    book_data.append([
        title,
        price,
        rating,
        availability,
        link
    ])

# Create DataFrame
df = pd.DataFrame(
    book_data,
    columns=[
        "Title",
        "Price",
        "Rating",
        "Availability",
        "Link"
    ]
)

# Display First 5 Records
print("========== SCRAPED BOOK DATA ==========\n")
print(df.head())

# Display Dataset Information
print("\n========== DATASET INFORMATION ==========\n")
print(df.info())

# Save Dataset to CSV File
df.to_csv("books_dataset_new.csv", index=False)

print("\nDataset Saved Successfully!")
print("File Name : books_dataset.csv")

# =========================================
# BASIC DATA ANALYSIS
# =========================================

print("\n========== BASIC ANALYSIS ==========\n")

# Total Books
print("Total Number of Books :", len(df))

# Highest Price
print("Highest Book Price :", df["Price"].max())

# Lowest Price
print("Lowest Book Price :", df["Price"].min())

# Average Price
print("Average Book Price :", round(df["Price"].mean(), 2))

# Rating Counts
print("\nBook Ratings Count:\n")
print(df["Rating"].value_counts())

# =========================================
# DATA VISUALIZATION
# =========================================

import matplotlib.pyplot as plt

# Select Top 10 Books
top_books = df.head(10)

# Create Figure
plt.figure(figsize=(15, 8))

# Create Bar Chart
plt.bar(top_books["Title"], top_books["Price"])

# Add Chart Title
plt.title("Top 10 Book Prices")

# Axis Labels
plt.xlabel("Book Titles")
plt.ylabel("Book Prices")

# Rotate Book Names
plt.xticks(rotation=45, ha='right')

# Adjust Bottom Space
plt.subplots_adjust(bottom=0.35)

# Show Graph
plt.show()


# =========================================
# PROJECT COMPLETED
# =========================================

print("\nWeb Scraping Task Completed Successfully!")
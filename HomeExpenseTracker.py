import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Global dataset to store expenses
expenses = []

def add_expense(date: str, category: str, amount: str, description: str):
    """
    Add a new expense to the dataset.

    This function validates the input data, ensures the date is in the correct format,
    and the amount is a positive number. If valid, the expense is added to the global dataset.

    Args:
        date (str): The date of the expense in YYYY-MM-DD format.
        category (str): The category of the expense (e.g., Food, Transport).
        amount (str): The amount of the expense as a string (e.g., '10.50').
        description (str): A brief description of the expense.
    """
    try:
        datetime.strptime(date, "%Y-%m-%d")
        amount = float(amount.replace(",", "."))
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        expenses.append({"date": date, "category": category, "amount": amount, "description": description})
        print("Expense added.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def save_to_json(filename: str):
    """
    Save the current expenses dataset to a JSON file.

    This function serializes the global expenses list and writes it to a JSON file.

    Args:
        filename (str): The name of the JSON file to save the data.
    """
    try:
        with open(filename, 'w', encoding="utf-8") as file:
            json.dump(expenses, file, indent=4)
        print(f"Data saved to file {filename}.")
    except IOError:
        print("Save error: Failed to write to file.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def load_from_json(filename: str):
    """
    Load expenses data from a JSON file.

    This function reads a JSON file and populates the global expenses list.

    Args:
        filename (str): The name of the JSON file to read data from.
    """
    try:
        global expenses
        with open(filename, 'r', encoding="utf-8") as file:
            expenses = json.load(file)
        print(f"Data loaded from file {filename}.")
    except FileNotFoundError:
        print(f"Error: File {filename} does not exist.")
    except json.JSONDecodeError:
        print(f"Error: File {filename} contains invalid JSON format.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def analyze_expenses():
    """
    Analyze the total and categorized expenses.

    This function calculates the total expenses and groups them by category, providing a summary.

    Args:
        None
    """
    try:
        if not expenses:
            raise ValueError("No expenses to analyze.")
        
        df = pd.DataFrame(expenses)
        total_expenses = df['amount'].sum()
        print(f"\nTotal expenses: {total_expenses:.2f}")
        
        category_summary = df.groupby('category')['amount'].sum()
        print("\nExpenses by category:")
        print(category_summary.to_string(index=True, header=False))
    except ValueError as e:
        print(f"Error: {e}")
    except KeyError:
        print("Error: Missing required data in expenses (e.g., 'amount' column).")
    except Exception as e:
        print(f"Unexpected error: {e}")

def visualize_expenses_pie():
    """
    Visualize the expenses as a pie chart.

    This function creates a pie chart showing the percentage distribution of expenses by category.

    Args:
        None
    """
    try:
        if not expenses:
            raise ValueError("No expenses to visualize.")
        
        df = pd.DataFrame(expenses)
        category_summary = df.groupby('category')['amount'].sum()
        
        plt.pie(category_summary, labels=category_summary.index, autopct='%1.1f%%')
        plt.title('Percentage of Expenses by Category')
        plt.show()
    except ValueError as e:
        print(f"Error: {e}")
    except ImportError:
        print("Error: Required library for visualization is missing. Install Matplotlib.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def visualize_expenses_bar():
    """
    Visualize the expenses as a bar chart.

    This function creates a bar chart showing the total expenses for each category.

    Args:
        None
    """
    try:
        if not expenses:
            raise ValueError("No expenses to visualize.")
        
        df = pd.DataFrame(expenses)
        category_summary = df.groupby('category')['amount'].sum()
        
        category_summary.plot(kind='bar', color='skyblue', title='Expenses by Category')
        plt.xlabel('Category')
        plt.ylabel('Amount')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main() -> None:
    """
    Main application menu for managing and analyzing expenses.

    This function provides a command-line interface for users to add expenses, save/load data, analyze,
    and visualize their expenses.

    Args:
        None
    """
    while True:
        try:
            print("\n--- Home Expense Tracker ---")
            print("1. Add expense")
            print("2. Save expenses to JSON")
            print("3. Load expenses from JSON")
            print("4. Analyze expenses")
            print("5. Visualize expenses - Pie Chart")
            print("6. Visualize expenses - Bar Chart")
            print("7. Exit")
            
            choice = input("Choose an option: ").strip()
            
            if choice == "1":
                date = input("Enter date (YYYY-MM-DD): ").strip()
                category = input("Enter category: ").strip()
                amount = input("Enter amount: ").strip()
                description = input("Enter description: ").strip()
                add_expense(date, category, amount, description)
            elif choice == "2":
                filename = input("Enter the filename to save (e.g., expenses.json): ").strip()
                save_to_json(filename)
            elif choice == "3":
                filename = input("Enter the filename to load (e.g., expenses.json): ").strip()
                load_from_json(filename)
            elif choice == "4":
                analyze_expenses()
            elif choice == "5":
                visualize_expenses_pie()
            elif choice == "6":
                visualize_expenses_bar()
            elif choice == "7":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()

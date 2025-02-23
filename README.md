# Python_ExpenseTracker_Matplotlib_Pandas
## Overview
Home Expense Tracker is a Python-based command-line application that helps users track, analyze, and visualize their expenses. Users can add expenses, save/load them from a JSON file, and generate summary reports and visualizations using Matplotlib and Pandas.

## Features
**Add Expenses:** Input expenses with date, category, amount, and description.

**Save & Load Data:** Store expenses in a JSON file and retrieve them later.

**Analyze Expenses:** View total spending and breakdown by category.

**Visualize Expenses:** 
* Pie Chart: Show percentage distribution by category. 
* Bar Chart: Display total expenses per category.

## Menu Options

**Add Expense**: Enter details of a new expense.

**Save Expenses to JSON**: Save current expenses to a file.

**Load Expenses from JSON**: Load expenses from a saved file.

**Analyze Expenses**: View total spending and category-wise breakdown.

**Visualize Expenses - Pie Chart**: Display expenses as a percentage pie chart.

**Visualize Expenses - Bar Chart**: Display expenses as a bar chart.

**Exit**: Quit the application.

## Data File

The folder includes a file expenses.json, which contains 100 randomly generated example expense records. This file can be used to test the application's functionalities.

## Error Handling

* Ensures correct date format (YYYY-MM-DD).

* Validates numerical input for the amount.

* Handles file errors when loading/saving JSON.

* Provides user-friendly error messages.

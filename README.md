# CSV to JSON Converter

A simple **CSV to JSON Converter** built using **Streamlit** and **Pandas**. This tool allows users to upload a CSV file, clean unnecessary columns (such as unnamed or empty columns), and convert the CSV data into a formatted JSON file. The user can then view the JSON output, copy it to the clipboard, or download it as a `.json` file.

## Features

- **Upload CSV**: Upload any CSV file.
- **Automatic Cleaning**: Automatically removes columns with names starting with "Unnamed" and any completely empty columns.
- **JSON Conversion**: Converts the cleaned CSV data to a formatted JSON object.
- **Copy JSON**: Copy the formatted JSON to the clipboard with one click.
- **Download JSON**: Download the formatted JSON as a `.json` file.

## Demo

![image](https://github.com/user-attachments/assets/ce4d8823-a8eb-4b17-9ea3-dc04280f403f)


## Prerequisites

- Python 3.x
- Streamlit
- Pandas
- pyperclip (for the clipboard copy functionality)

## Installation

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/MuhammadAhmed-0/csv-to-json-converter.git

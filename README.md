# Automated Data Extraction and Transformation Tool

## Overview

This tool is designed to automate the process of extracting specific data from HTML content stored in an Excel file and transforming it into a structured JSON format. It then processes these JSON objects to create and export a well-organized Excel file. This README document provides detailed instructions and explanations for setting up and using this tool.

![Project Image Overview](https://github.com/DevRex-0201/Project-Images/blob/main/Py-Automatic-Data-Extraction-Transformation.png)

## Prerequisites

Before using this tool, ensure you have the following prerequisites installed:

1. **Python:** The tool is written in Python, so ensure you have Python installed on your machine.
2. **Pandas Library:** Used for data manipulation and analysis.
3. **OpenAI API Key:** This tool uses OpenAI's GPT model for data extraction from HTML content.
   
   Install pandas using pip:
   ```bash
   pip install pandas
   ```

## Installation

1. **Clone the Repository:**
   Download or clone the tool's repository to your local machine.

2. **Install Dependencies:**
   Navigate to the tool's directory and install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **OpenAI API Key:**
   Set your OpenAI API key in the code. Replace `'your_api_key_here'` with your actual API key.

## Usage

1. **Prepare the Input File:**
   - Place your Excel file (with HTML content) in the tool's directory. Ensure it follows the format used in `source.xlsx`.

2. **Run the Tool:**
   - Execute the Python script to start the data extraction process:
     ```bash
     python script_name.py
     ```

3. **Output:**
   - The script will create a text file (`extracted_data.txt`) containing the extracted JSON data.
   - It will then transform this data into an Excel file (`output_data.xlsx`).

## How It Works

1. **Data Extraction:**
   - The tool reads HTML content from an Excel file.
   - It then uses OpenAI's GPT model to extract specified data fields from this HTML content, outputting them in JSON format.

2. **Data Transformation:**
   - The extracted JSON data is read and processed.
   - Specific fields are extracted and transformed into a structured Excel format.

## Limitations

- The tool is dependent on the structure of the HTML content. Changes in the HTML structure may require adjustments in the data extraction logic.
- The OpenAI API has usage limits and costs associated with it.

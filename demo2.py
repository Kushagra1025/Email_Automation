import csv
import email_functions
def read_column_to_list(file_path, column_name):
    """
    Reads a specific column from a CSV file and stores it in a list.
    
    Args:
        file_path (str): Path to the CSV file.
        column_name (str): The name of the column to extract.
    
    Returns:
        list: A list containing the values of the specified column.
    """
    data_list = []
    
    try:
        # Open and read the CSV file
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            
            # Extract the column data
            for row in reader:
                data_list.append(row[column_name])
                
    except KeyError:
        print(f"Column '{column_name}' not found in the file.")
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return data_list

# Example usage
file_path = 'accounts.csv'  # Replace with the actual file path
column_name = 'email'        # Replace with the desired column name
data = read_column_to_list(file_path, column_name)
print(data)
email_functions.send_common_emails(data,"Test Email","Hi, This is a test email.")

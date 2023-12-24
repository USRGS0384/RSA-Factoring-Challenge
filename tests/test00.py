import os

# Ensure the 'tests' directory exists
os.makedirs("tests", exist_ok=True)

# Specify the full path to the file
file_path = os.path.join("tests", "test00")

# Open the file in write mode
with open(file_path, "w") as file:
    # Write the numbers to the file, one per line
    numbers = "4\n12\n34\n128\n1024\n4958\n1718944270642558716715\n9\n99\n999\n9999\n9797973\n49\n239809320265259"
    file.write(numbers)

# Print a confirmation message
print(f"File '{file_path}' created successfully!")

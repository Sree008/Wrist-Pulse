import subprocess

# Execute the first Python code and capture the output
process1 = subprocess.Popen(["python", "D:\\Final_Project_Working\\data_collection.py"], stdout=subprocess.PIPE)
output1, _ = process1.communicate()

# Print the output of the first program
print(output1.decode())

# Execute the second Python code and capture the output
process2 = subprocess.Popen(["python", "D:\\Final_Project_Working\\filter_raw_signals.py"], stdout=subprocess.PIPE)
output2, _ = process2.communicate()

# Print the output of the second program
print(output2.decode())

# Execute the third Python code and capture the output
process3 = subprocess.Popen(["python", "D:\\Final_Project_Working\\feature_extraction2.py"], stdout=subprocess.PIPE)
output3, _ = process3.communicate()

# Print the output of the third program
print(output3.decode())

# Execute the fourth Python code and capture the output
process4 = subprocess.Popen(["python", "D:\\Final_Project_Working\\normalize_data.py"], stdout=subprocess.PIPE)
output4, _ = process4.communicate()


# Execute the fifth Python code and capture the output
process5 = subprocess.Popen(["python", "D:\\Final_Project_Working\\predict_from_algo.py"], stdout=subprocess.PIPE)
output5, _ = process5.communicate()

print(output5.decode())

# ...




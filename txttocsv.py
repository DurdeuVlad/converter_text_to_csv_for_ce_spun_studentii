import csv

MAX_ANSWERS=8

input_filename = 'input.txt'
output_filename = 'output.csv'

# Open the input file and read the lines
with open(input_filename, 'r') as f:
    lines = f.readlines()

# Create a list to hold the data for the output CSV file
output_data = []

# Loop through the lines in the input file
i = 0
while i < len(lines):
    print("SUNTEM PE LINIA", i)
    # Check if this is a question line
    if lines[i].find('.'):
        question = lines[i].strip()
        answers = []
        points = []
        # Loop through the next 5 lines to get the answers and points
        for j in range(i+1, i+MAX_ANSWERS-1):
            print("SUNTEM cu j PE LINIA", j)
               
            try:
                answer, point = lines[j].strip().split()
                answer = answer.replace('—', '')
                answer = answer.replace('â€”', '')
                answer = answer.replace('\"\"', '')
                print(". ANSWER: "+ answer+ " POINT: "+point)
                
                answers.append(answer)
                answers.append(point)
            
            except NameError:
                print("Am gasit NameError")
                break
            except ValueError:
                print("Am gasit ValueError")
                break
            except IndexError:
                print("Am gasit IndexError")
                break

            # Remove the dashes from the answer
        # Add the data to the output list
        row = [question] + answers
        if row[0]!='':
            print("Bagam linia: ", row)
            output_data.append(row)
        
        # Move to the next question
        print('Mergem pe urmatoarea linie')
        i += j-i
    else:
        # Move to the next line
        i += 1

# Write the output data to the CSV file
with open(output_filename, 'w', newline='') as f:
    writer = csv.writer(f)
    # Write the headers
    header = ['question']
    for i in range(0, MAX_ANSWERS):
        header.append('answer')
        header.append('points')
    writer.writerow(header)
    # Write the data
    writer.writerows(output_data)

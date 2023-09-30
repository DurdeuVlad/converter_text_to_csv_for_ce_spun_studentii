import csv

MAX_ANSWERS=8

input_filename = 'input.txt'
output_filename = 'output.csv'

# Open the input file and read the lines
try:
    f = open(input_filename, 'r')
    lines = f.readlines()
except FileNotFoundError:
    print("File not found, creating new.")
    f = open(input_filename, 'w')
    exit(1)
#with open(input_filename, 'r') as f:
#    lines = f.readlines()


# Create a list to hold the data for the output CSV file
output_data = []

# Loop through the lines in the input file
i = 0
while i < len(lines):
    #print("SUNTEM PE LINIA", i)
    # Check if this is a question line
    if lines[i].find('.')!=-1:
        question = lines[i].strip().replace(",",'')
        print("Question detected: "+ question)
        answers = []
        points = []
        # Loop through the next 5 lines to get the answers and points
        for j in range(i+1, i+MAX_ANSWERS):
           # print("SUNTEM cu j PE LINIA", j)
            try:
               if lines[j].find('.')!=-1:
                   break
            except IndexError:
                break
            try:
                line = lines[j].strip().replace('-', ' ').replace('â€”', '').replace('\"\"', '').replace(",",'').replace("   ",'').replace("*", '')
                answer, point = line.rsplit(' ', 1)
                print(". ANSWER: "+ answer+ " POINT: "+point)
                answers.append(answer)
                answers.append(point)
                
                    
            
            except NameError:
                #print("Am gasit NameError")
                break
            except ValueError:
                #print("Am gasit ValueError")
                break
            except IndexError:
                #print("Am gasit IndexError")
                break

            # Remove the dashes from the answer
            
        # Sort answers
        
        # Add the data to the output list
        questionnew = ""
        try:
            questionnew=answers.pop(0)
            questionnew+=" "+answers.pop(0)
            answer_tuples = zip(*[iter(answers)]*2)  # create a list of tuples
            sorted_tuples = sorted(answer_tuples, key=lambda x: int(x[1]), reverse=True)  # sort the tuples by points
            sorted_answers = []
            # sorted_answers.append(questionnew)
            for answer, points in sorted_tuples:
                sorted_answers.append(answer)
                sorted_answers.append(points)

            print("Answers: ", answers)
            print("sorted_tuples: ", sorted_tuples)
            print("sorted_answers: ", sorted_answers)
        except IndexError:
            print("Index error")
        except ValueError:
            print("ValueError")

        #sorted_answers.insert(0,questionnew)
        if question=="":
            row = [questionnew]+sorted_answers
        else:
            row = [question]+sorted_answers
        
        if row!='' and row[0]!='':
            print("Bagam linia: ", row)
            output_data.append(row)

        
            
        
        # Move to the next question
        #print('Mergem pe urmatoarea linie')
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

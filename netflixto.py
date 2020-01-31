#modules
import csv
import os

#prompt video you want to watch
movie_title = input('what movie do you want to wtch ? \n')

#initially status of the movie, if cahnges to True, movies is on netflix
movie_status = False

#provide path to file with movies
csvpath = os.path.join('..','Resources','netflix_ratings.csv')
print(csvpath)

#open cv file, opening file only but not reading yet
with open(csvpath, newline='',) as csvfile:
    movie_reader = csv.reader(csvfile, delimiter=',' )
      
 #this step is responsible for reading the file LINE BY LINE as a set of lists with each word indexed!
    for row in movie_reader:
      
    #row[0] means 1st word in the list of row that is read
    # "if" goes line by line
     
        if row[0] == movie_title:
            print(f'{row[0]} is rated {row[1]} with a ratings {row[0]}')
            #if the movie is in line that is red we print statement, change status (no efect for this loop) and break
            movie_status = True
            break
            #if the movie is not i the line we keep cycling until find it
    
    #after finishing cycling we leave the loop and check the status of the movie
    #if the status of the movie was changed to "True" the next statement shouldn't be executed, 
    #if the status of the movie was NOT changed and remains "False" the next test will post a message
    if movie_status == False:
        print(f"we don't have '{movie_title}'")
            
    
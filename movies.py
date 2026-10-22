def count_movies(filename):
    fili = open(filename, "r")
    line = fili.readline()
    number = 0
    while line != '':
        number += 1
        line = fili.readline()
    fili.close()
    return number
filename = "movies.txt"
print("Number of movies:", count_movies(filename))

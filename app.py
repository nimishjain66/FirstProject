movies = []


def menu():
    user_input = input("Enter a to add movie , l to see your movie, f to find , & q to quit : ")
    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movie(movies)
        elif user_input == 'f':
            find_movie()

        else:
            print("enter the value again ")

        user_input = input("Enter a to add movie , l to see your movie, f to find , & q to quit : ")


def add_movie():
    name = input("Enter the movie name : ")
    director = input("Enter the director name : ")
    year = input("Enter the year : ")

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })


def show_movie(movie_list):
    for movie in movie_list:
        show_movie_detail(movie)


def show_movie_detail(movie):
    print(f"\nName : {movie['name']}")
    print(f"Released Year : {movie['year']}\n")
    print(f"Director : {movie['director']}\n")


def find_movie():
    find_by = input("How you want to search year ,director , name : ")
    looking_for = input("Enter the parameter to be search : ")
    found_movies=find_by_attribute(movies,looking_for,lambda x:x[find_by])
    show_movie(found_movies)


def find_by_attribute(item,expected,finder):
    found = []
    for i in item:
        if finder(i) == expected:
            found.append(i)
    return found




menu()

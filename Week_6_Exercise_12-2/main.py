#!/usr/bin/env python3
# Jeff Bohn
# 9/26/2024
# Week_6_Lab_2
# Chapter 12 - Working with Dictionaries


#############  Exercise_12-2  :  Enhance the Movie List 2D Program  #############


def list(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
        return
    else:
        for i, movie in enumerate(movie_list):
            print(f"{i + 1}. {movie['name']} ({movie['year']})")


def add(movie_list):
    name = input("Name: ")
    year = input("Year: ")
    movie = {"name": name.title(), "year": year.title()}
    movie_list.append(movie)
    print(f"{movie['name']} was added.\n")


def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number - 1)
        print(f"{movie['name']} was deleted.\n")


def display_menu():
    print("\nCOMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()


def main():
    movie_list = [
        ["Monty Python and the Holy Grail", 1975],
        ["On the Waterfront", 1954],
        ["Cat on a Hot Tin Roof", 1958],
        ["Star Wars", 1977],
    ]

    movie_list = dict(movie_list)
    movie_list2 = []
    for i, obj in movie_list.items():
        movie_list2.append({"name": i, "year": obj})
    # print(movie_list2)
    movie_list = movie_list2

    display_menu()

    while True:
        command = input("Command: ").lower()
        if command == "list":
            list(movie_list)
        elif command == "add":
            add(movie_list)
        # print(movie_list)
        elif command == "del":
            delete(movie_list)
        # print(movie_list)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!\n")


if __name__ == "__main__":
    main()


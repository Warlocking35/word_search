def word_search():
    """
    The user can input any phrase or passage, and also the word
    that will be searched for.

    :return: The word and how many were found.
    """

    connected_word = []  # Empty list that the matching words fall into
    number_cw = 0  # The amount of times a word is found

    while True:  # ends if the input is 0
        print("Text to search (Press 0 to exit): ")
        phrase_input = str(input("-> ")).casefold()
        if phrase_input == '0':  # Checks to see if the input is 0
            break

        phrase_split = phrase_input.split()  # Creates a new list

        print("Word to search for (Press 0 to exit): ")
        word_selection = str(input("-> ")).casefold()
        if word_selection == '0':  # Checks to see if the input is 0
            break

        for words in phrase_split:
            if word_selection in words:
                connected_word.append(words)
                number_cw += 1

        print(f"{word_selection}: found {number_cw} times")
        number_cw = 0
    print("Come again!")


word_search()

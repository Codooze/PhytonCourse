authors = """Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,
Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"""

author_names = authors.split(',')

print(author_names)

print("Ahora solo los apellidos:")
author_last_names = []
for name in author_names:
    author_last_names.append(name.split()[-1])

print(author_last_names)


def strip_and_join():
    love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ',
                        'you lay down your arms', '           like flowering mines    ', '\n', '   to conquer me home.    ']

    love_maybe_lines_stripped = []

    for line in love_maybe_lines:
        love_maybe_lines_stripped.append(line.strip())

    print(love_maybe_lines_stripped)
    print()
    love_maybe_full = '\n'.join(love_maybe_lines_stripped)

    print(love_maybe_full)


# *strip_and_join()


def string_for_loops():  # !
    highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

    # print(highlighted_poems)

    highlighted_poems_list = highlighted_poems.split(",")
    # print(highlighted_poems_list)
    highlighted_poems_stripped = []
    for poem in highlighted_poems_list:
        highlighted_poems_stripped.append(poem.strip())
    # print(highlighted_poems_stripped)

    highlighted_poems_details = []

    for poem in highlighted_poems_stripped:
        highlighted_poems_details.append(poem.split(":"))

        titles = []
        poets = []
        dates = []
    print("\n", highlighted_poems_details)
    for poem in highlighted_poems_details:
        titles.append(poem[0])
        poets.append(poem[1])
        dates.append(poem[2])

    for i in range(0, len(highlighted_poems_details)):
        print("The poem {} was published by {} in {}".format(
            titles[i], poets[i], dates[i]))


string_for_loops()

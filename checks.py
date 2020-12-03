# Check win
def check_victoire(tab, signe):
    win_row = check_victoire_row(tab, signe)
    win_column = check_victoire_column(tab, signe)
    win_diagonal = check_victoire_diagonal(tab, signe)
    if win_row == 1 or win_column == 1 or win_diagonal == 1:
        return 1
    else:
        return 0

# Check wins on a row
def check_victoire_row(tab, signe):
    for row in tab:
        number_row = 0
        for element in row:
            if element == signe:
                number_row += 1
            else :
                break
        if number_row == 3:
            return 1
    return 0

# check wins on a column
def check_victoire_column(tab, signe):
    for row in tab:
        for element in row:
            if element == signe:
                result = check_next_column(tab, signe, tab.index(row), row.index(element), 1) # Result of numbers aligned
                if result == 3: # If 3 numbers aligned, it's a win !
                    return 1
    return 0

# recursive function for column checks
def check_next_column(tab, signe, index_row, index_element, aligned):
    if index_row+1 < len(tab): # If element exist
        if tab[index_row+1][index_element] == signe: # If it's the sign
            aligned += 1 # One more sign is aligned
            if aligned != 3: # If not enought signs aligned
                aligned = check_next_column(tab, signe, index_row+1, index_element, aligned) # Redo
                return aligned # return aligned
            else:
                return aligned # else return aligned for win
        else:
            return 0
    else:
        return 0

# check wins on diagonal
def check_victoire_diagonal(tab, signe):
    for row in tab:
        for element in row:
            if element == signe:
                result = check_next_diagonal(tab, signe, tab.index(row), row.index(element),1)  # Result of numbers aligned
                if result == 3:  # If 3 numbers aligned, it's a win !
                    return 1
    return 0

# recursive function for column checks
def check_next_diagonal(tab, signe, index_row, index_element, aligned):
    if index_row + 1 < len(tab):  # If element exist
        if index_element + 1 < len(tab[index_row + 1]):
            if tab[index_row + 1][index_element+1] == signe:  # If it's the sign
                aligned += 1  # One more sign is aligned
                if aligned != 3:  # If not enought signs aligned
                    aligned = check_next_diagonal(tab, signe, index_row+1, index_element+1, aligned)  # Redo
                    return aligned  # return aligned
                else:
                    return aligned  # else return aligned for win
            else:
                return 0
        else:
            return 0
    else:
        return 0

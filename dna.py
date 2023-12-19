#  DNA Matching
#  
#  Copyright (c) 2023 Alessandro Amatucci Girlanda
#  
#  This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#  4.0 International License. To view a copy of this license, visit
#  http://creativecommons.org/licenses/by-nc-sa/4.0/ or send a letter to Creative
#  Commons, PO Box 1866, Mountain View, CA 94042, USA.
#  
#  You are free to:
#    - Share — copy and redistribute the material in any medium or format
#    - Adapt — remix, transform, and build upon the material
# 
#  Under the following terms:
#    - Attribution — You must give appropriate credit, provide a link to the license, and
#                   indicate if changes were made. You may do so in any reasonable manner,
#                   but not in any way that suggests the licensor endorses you or your use.
#    - NonCommercial — You may not use the material for commercial purposes.
#    - ShareAlike — If you remix, transform, or build upon the material, you must
#                   distribute your contributions under the same license as the original.
# 
#  No additional restrictions — You may not apply legal terms or technological measures
#  that legally restrict others from doing anything the license permits.
#
#  Acknowledgment:
#  This repository includes the Databases and Sequences folders developed by Harvard University CS50.


import csv
import sys


def main():
    # Check for command-line usage
    len_argv = len(sys.argv)
    if len_argv != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # Read database file into a variable
    data_file = open(sys.argv[1], "r")
    data_reader = csv.DictReader(data_file)

    data_dict = list()
    for row in data_reader:
        data_dict.append(row)

    # Store keys in a list
    # Remove the "name" key
    str_list = list(data_dict[0].keys())
    str_list.pop(0)

    # Store list length
    str_list_len = len(str_list)

    # Read DNA sequence file into a variable
    dna_file = open(sys.argv[2], "r")
    dna_reader = dna_file.read()

    # Find longest match of each STR in DNA sequence
    # e.g., repeats = longest_match(dna_reader, "AGATC")
    dna_dict = dict()
    for str in str_list:
        dna_dict[str] = longest_match(dna_reader, str)

    # Check database for matching profiles
    dna_match = "No match"
    for person in data_dict:
        for str in str_list:
            if int(person[str]) != dna_dict[str]:
                break
            elif str == str_list[str_list_len - 1]:
                dna_match = person["name"]
        if dna_match != "No match":
            break

    print(dna_match)

    # Close files before terminating the program
    data_file.close()
    dna_file.close()

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()

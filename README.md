# DNA Matching 🧬👥
## Introduction 📖
DNA is a sequence of molecules (nucleotides) arranged into a particular shape. Each nucleotide of DNA contains one of four different bases: adenine (A), cytosine (C), guanine (G), or thymine (T). Some portions of this sequence are the same across almost all humans, but other portions of the sequence have a higher genetic diversity and thus vary more across the population.

DNA tends to have high genetic diversity in Short Tandem Repeats (STRs). An STR is a short sequence of DNA bases that tends to repeat consecutively numerous times at specific locations inside of a person’s DNA. The number of times any particular STR repeats varies among individuals. In the DNA samples below, for example, Alice has the STR AGAT repeated 4 times in her DNA, while Bob has the same STR repeated 5 times.

```
Alice - CTAGATAGATAGATAGATGACTA
Bob - CTAGATAGATAGATAGATAGATT
```

In its simplest form, a DNA database can be formatted as a CSV file, where each row corresponds to an individual, and each column corresponds to a particular STR.

|Name   |AGAT   |AATG   |TATC   |
|-      |:-:    |:-:    |:-:    |
|Alice  |28     |42     |14     |
|Bob    |17     |22     |19     |
|Charlie|36     |18     |25     |

The data in the above table, for example, shows that Alice has the sequence AGAT repeated 28 times consecutively somewhere in her DNA, the sequence AATG repeated 42 times, and TATC repeated 14 times.

The program takes a sequence of DNA and a CSV file containing STR counts for a list of individuals and then outputs to whom the DNA belongs (a no match is also possible).

## How to Run the Program 🗔
### Programming Language Needed ⌨️
```
Python3
```
### Execute ▶️
Start by cloning the repository in your local machine.

```
git clone https://github.com/ErTucci674/dna-matching.git
```

Choose a _database_ file and a _sequences_ file and enter the following line of code:

```
python dna.py (data.csv path) (sequence.txt path)
```
e.g.
```
python dna.py databases/large.csv sequences/6.txt
```

## Files and Code 🗃️
### Lists and Tables 📄
In the `sequences` folder there are 20 different DNA series that can be used to test the program. Each sequence is stored in a text-format file.

In the `databases` folder there are two _CSV_ files: `large.csv`, `small.csv`. The two files contain tables with entities' DNA series similar to the one shown in the _Introduction_.

### Main File ⚡
The main file that manages all the program is `dna.py`. The libraries `csv` and `sys` are used to read the _CSV_ files and the user's input inserted in the terminal.

The program requires as it first command-line argument the _CSV_ file path containing the STR counts for a list of individuals. As its second command-line arguments, instead, the name of the text file containing the DNA sequence to identify.

```python
len_argv = len(sys.argv)
if len_argv != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    sys.exit(1)
```

The _if statement_ above checks if the user's input contains the number of requested 'items' with the `sys` library.

The STR lines are stored as a dictionary in a table `data_dict` through the `csv` library.

```python
data_file = open(sys.argv[1], "r")
data_reader = csv.DictReader(data_file)

data_dict = list()
for row in data_reader:
    data_dict.append(row)
```

The second file is read by the `read()` function instead. The `longest_match()` function is then used to count each STR of the given series through a _for loop_.

The last _for loop_ checks whether the combination is present in the given _CSV_ file. In case of a match, the corresponding name is printed out, otherwise a _No match_ is shown.

```python
dna_match = "No match"
for person in data_dict:
    for str in str_list:
        if int(person[str]) != dna_dict[str]:
            break
        elif str == str_list[str_list_len - 1]:
            dna_match = person["name"]
    if dna_match != "No match":
        break
```

## Reference Links 🔗
Databases and Sequences files - [Harvard University Online Course (edx50)](https://cs50.harvard.edu/x/2023/psets/6/dna/)

## Licence 🖋️
This project is licensed under the terms of the Attribution-NonCommercial-ShareAlike 4.0 International.
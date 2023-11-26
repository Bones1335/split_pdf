# Split-PDF

## Functionality

Take in a large pdf file based on the user's desired working directory input and output any number of split files necessary based on every nth split from user input.

- ***For example: a 6 page pdf split every 4th page will output 2 PDF files - the 1st with 4 pages and the second with only 2 pages.***

## How to use

0. make sure the working directory has a CSV file called "names.csv" that follows the convention "NOM, Prénom" for the column titles.
    - **NOTE: this feature will be updated to be a little more dynamic**
1. run `python main.py`
2. type the full path of the desired working directory
3. type the name of the file to be split
4. the rest happens automatically
    - first, the file is split
    - second, the original PDF is moved to the trash
    - third, the filenames in the working directory are passed to the renaming function
    - fourth, the renaming function takes in the working directory's CSV file to rename every PDF, in order, based on the CSV file's naming convention. 
        - ***see 'How to use' point 0 for the current naming convention system of the CSV file***

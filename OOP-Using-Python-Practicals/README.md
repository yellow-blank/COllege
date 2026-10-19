<div align="center">

# â™¡ Object Oriented Programming Using Python

### Semester 1 Â· Practical Assignment

*A small collection of Python practicals, organised with care.*

<img src="https://img.shields.io/badge/Python-3.10%2B-E7D7C8?style=flat-square&logo=python&logoColor=59483F" alt="Python 3.10+" />
<img src="https://img.shields.io/badge/Practicals-13-DCE8D8?style=flat-square&labelColor=F5EFE8&color=DCE8D8" alt="13 practicals" />
<img src="https://img.shields.io/badge/Packages-No%20external%20packages-E8DFF0?style=flat-square" alt="No external packages" />

[Practicals](#-practicals) Â· [How to Run](#-how-to-run) Â· [Submission Details](#-student-and-course-details)

</div>

---

## ðŸŒ· About this repository

This repository contains the **13 practical programs** from the *Object Oriented Programming using Python* practical list. Each practical is saved in its own Python file so it is easy to read, run, test, and review during a lab submission or viva.

The programs cover Python basics, conditions and loops, functions, strings, lists, files, dictionaries, tuples, exceptions, and a `Point` class.

## ðŸ—‚ï¸ Repository structure

```text
OOP-Using-Python-Practicals/
â”œâ”€â”€ README.md
â”œâ”€â”€ SUBMISSION_CHECKLIST.md
â”œâ”€â”€ .gitignore
â””â”€â”€ practicals/
    â”œâ”€â”€ 01_quadratic_roots.py
    â”œâ”€â”€ 02_prime_numbers.py
    â”œâ”€â”€ 03_star_pyramids.py
    â”œâ”€â”€ 04_character_classifier.py
    â”œâ”€â”€ 05_string_operations.py
    â”œâ”€â”€ 06_swap_first_n_characters.py
    â”œâ”€â”€ 07_substring_indices.py
    â”œâ”€â”€ 08_even_integer_cubes.py
    â”œâ”€â”€ 09_file_operations.py
    â”œâ”€â”€ 10_point_class.py
    â”œâ”€â”€ 11_dictionary_cubes.py
    â”œâ”€â”€ 12_tuple_operations.py
    â”œâ”€â”€ 13_name_validation_exceptions.py
    â””â”€â”€ sample.txt
```

> The folder shown above is the assignment folder structure. If you place it inside an existing repository, keep the relative links working or update them to match your folder name.

## ðŸ“š Practicals

| No. | Practical / Topic | Source file |
|:--:|---|---|
| 01 | Find the roots of a quadratic equation, including complex roots and the linear case | [`01_quadratic_roots.py`](practicals/01_quadratic_roots.py) |
| 02 | Check whether `n` is prime, list primes up to `n`, and generate the first `n` primes using functions | [`02_prime_numbers.py`](practicals/02_prime_numbers.py) |
| 03 | Print a star pyramid and its reverse pyramid | [`03_star_pyramids.py`](practicals/03_star_pyramids.py) |
| 04 | Classify a character; identify letter case or spell out a digit | [`04_character_classifier.py`](practicals/04_character_classifier.py) |
| 05 | Find character frequency, replace a character, remove its first occurrence, and remove all occurrences | [`05_string_operations.py`](practicals/05_string_operations.py) |
| 06 | Swap the first `n` characters of two strings | [`06_swap_first_n_characters.py`](practicals/06_swap_first_n_characters.py) |
| 07 | Return all starting indices of a substring, or `-1` when it is absent | [`07_substring_indices.py`](practicals/07_substring_indices.py) |
| 08 | Cube even integers from a mixed-type list using a `for` loop and list comprehension | [`08_even_integer_cubes.py`](practicals/08_even_integer_cubes.py) |
| 09 | Count characters, words, and lines; count character frequencies; reverse word order; split even/odd lines into files | [`09_file_operations.py`](practicals/09_file_operations.py) |
| 10 | Define a `Point` class and calculate the distance between two points | [`10_point_class.py`](practicals/10_point_class.py) |
| 11 | Create and print a dictionary mapping numbers 1â€“5 to their cubes | [`11_dictionary_cubes.py`](practicals/11_dictionary_cubes.py) |
| 12 | Perform the required tuple operations, including `t2 + t1`, maximum, and minimum | [`12_tuple_operations.py`](practicals/12_tuple_operations.py) |
| 13 | Validate a name and raise/handle exceptions for digits or special characters | [`13_name_validation_exceptions.py`](practicals/13_name_validation_exceptions.py) |

## ðŸ› ï¸ Requirements

- **Python 3.10 or newer**
- **VS Code** or another Python editor
- No third-party packages are required

## â–¶ï¸ How to run

1. Download or clone the repository.
2. Open the project folder in VS Code.
3. Open **Terminal â†’ New Terminal**.
4. Run the practical you want to test. For example:

   ```bash
   python practicals/01_quadratic_roots.py
   ```

   On some systems, use `python3` or (on Windows) `py` instead of `python`.

5. Follow the prompts and enter the requested values in the terminal.

Each program can be run independently. Replace the example filename with the practical you want to run.

## ðŸ“ Notes for Practical 09 â€” File handling

- [`sample.txt`](practicals/sample.txt) is included as a sample input file.
- When Practical 09 asks for a file path, press **Enter** to use `sample.txt`.
- The program saves even-numbered lines in `practicals/File1` and odd-numbered lines in `practicals/File2`.
- `File1` and `File2` are generated outputs and are ignored by `.gitignore`; they do not need to be committed unless your teacher asks for them.

## ðŸŽ“ Student and course details

Fill in the placeholders below before submitting, if your college requires these details.

| Field | Details |
|---|---|
| Student name | `[Your full name]` |
| Roll number / Enrollment number | `[Your roll number]` |
| Course / Programme | `[Your course name]` |
| Semester | `1` |
| Subject | `Object Oriented Programming using Python` |
| Submitted to | `[Faculty name]` |
| College / Department | `[College and department name]` |
| Academic session | `[Academic year]` |

## âœ… Before submitting

- [ ] Replace the student/course placeholders above, if required.
- [ ] Check that all 13 practicals match the teacher's question sheet.
- [ ] Run each program in VS Code with suitable inputs.
- [ ] Review the outputs and be ready to explain the logic during a practical or viva.
- [ ] Commit and push the files to GitHub.
- [ ] Open the GitHub repository in a browser and confirm that the README and source files are visible.

## ðŸ¤ A little Python reminder

> Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex.
>
> â€” *The Zen of Python*

<div align="center">

Made with care for learning and practice  
**~ yellow.Tushar ðŸ¤**

</div>

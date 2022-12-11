# Python exercises

These are Python exercises done by me on a course called [Programming for Linguists](https://studies.helsinki.fi/opintotarjonta/cu/hy-CU-117878680-2021-08-01/KIK-LG208/Ohjelmointia_lingvisteille) which focuses less on mathematical calculations and more on string and text processing. The exercises are developed mostly using [TDD](https://en.wikipedia.org/wiki/Test-driven_development). I am using [pytest](https://pytest.org) as a unit testing framework.

## How to run?

You can run the snippets and tests from the root folder.

To run a single snippet:

```
python src/assignment_0_1.py
```

To run the tests (use -v for more info on console):

```
pytest -s -v tests
```

## Assignments

| Assignment | Code | Test |
| ---------- | ---- | ---- |
| 0.1 | [What's your name?](src/assignment_0_1.py) | [Test input](tests/test_input.py) |
| 1.1 | [How much does it cost?](src/assignment_1_1.py) | [Test store](tests/test_store.py) |
| 1.2 | [Understanding division and modulo](src/assignment_1_2.py) | [Test division](tests/test_division.py) |

## Some links

- Book: [How to Think Like a Computer Scientist](http://openbookproject.net/thinkcs/python/english3e/)
- Book: [Natural Language Processing with Python](https://www.nltk.org/book/)
- Course videos: [Ohjelmoinnin peruskurssi Y1](https://mycourses.aalto.fi/course/view.php?id=28145&section=3)
Library Management System – Software Engineering Assignment


This project is developed as part of the Software Engineering course assignment.
It demonstrates Agile sprint-based development, Git version control, unit testing, and traceability practices.

Project Overview


The Library Management System supports basic library operations including:

Adding books with unique identifiers

Borrowing and returning books

Generating a library report

Validating functionality using unit tests

The system is implemented incrementally across multiple sprints following Agile methodology.

Sprint Breakdown
Sprint 1 – Book Registration (v0.1)

Add books with book ID, title, and author

Prevent duplicate book registration

Unit tests for book registration

Sprint 2 – Borrow and Return Books (v0.2)

Borrow available books

Prevent borrowing unavailable books

Return borrowed books

Unit tests for borrowing and return functionality

Sprint 3 – Library Report Generation (v0.3)

Generate library report

Project Structure

library-se/
├── docs/
│   ├── USER_STORIES.md
│   └── TRACEABILITY.md
├── src/
│   └── library.py
├── tests/
│   └── test_library.py
├── .gitignore
└── README.md

Running Unit Tests:

python -m unittest discover -s tests -p "test_*.py" -v

Version Tags:


v0.1 – Sprint 1: Book registration

v0.2 – Sprint 2: Borrow and return functionality

v0.3 – Sprint 3: Library report and final version

Technologies Used:


Python

Git and GitHub

unittest testing framework


Author

Rahul Sidhu




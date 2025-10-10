# Copilot Instructions for uts2025-32555

This project is a teaching codebase for the subject "32555 Fundamentals of Software Development - Spring 2025". It is organized by week, with each week containing Python scripts for exercises, labs, and assignments.

## Project Structure & Key Directories
- `src/weekXX/`: Weekly folders (e.g., `week03`, `week04`, ...) contain Python files for that week's exercises and labs.
- `src/week10/`: Example of a more structured mini-project with `model.py`, `controller.py`, and view files, following a basic MVC pattern.
- `customers.data`, `data.csv`, etc.: Example data files for exercises.
- `README.md`: Minimal, not a source of workflow documentation.

## Coding Patterns & Conventions
- Each week is self-contained; scripts are not tightly coupled across weeks.
- Naming: `labXX.py` for labs, `excerciseX.Y.py` for exercises, `testStudent.py` for student test scripts.
- Week 10 uses a simple MVC structure:
  - `model.py`: Data and business logic
  - `controller.py`: Orchestrates logic between model and view
  - `main_view.py`, `frame_view.py`: UI components
- Most scripts are standalone and use procedural or basic OOP (see `Bank` class in `week03/lab3.py`).

## Developer Workflows
- No build system or dependency manager; run scripts directly with Python 3.
- Example: `python3 src/week03/lab3.py`
- No formal test framework; some scripts (e.g., `testStudent.py`) contain ad-hoc tests.
- No CI/CD or linting configured.

## Project-Specific Practices
- Input/output is often via `input()` and `print()` for interactive exercises.
- Data files are read directly from the same directory as the script.
- No external dependencies expected; keep code portable and simple.
- Docstrings and comments are encouraged for clarity, especially in OOP code.

## Integration & Extensibility
- If adding new weeks, follow the existing folder and file naming conventions.
- For new structured projects, consider the simple MVC pattern from `week10` as a guide.
- Avoid introducing complex frameworks or dependencies unless required by the curriculum.

## Examples
- See `src/week03/lab3.py` for a basic OOP exercise (Bank class).
- See `src/week10/` for a simple MVC mini-project.

---
For questions about project structure or conventions, consult the subject coordinator or refer to the latest weekly folders for examples.

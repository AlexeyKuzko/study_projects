# Contributing Guide

Overview
- This repository contains multiple independent Python QA automation subprojects and practice tasks. Each subproject has its own dependencies and test commands.

Getting started
- Prerequisites: Python 3.8+ (or as required by the subprojects), git, and pytest installed.
- From repository root, you can run all tests via the root runner: `bash scripts/ci_run_all_tests.sh`.
- To contribute a new subproject, add it under an existing folder (e.g., ya_praktikum_aqa_projects/new_subproject) with its own README, tests/, and requirements.txt if Python-based.

Running tests locally
- The recommended workflow is to use the root runner to exercise all projects:
  - Ensure you have the latest code: `git pull`.
  - Run: `bash scripts/ci_run_all_tests.sh`.
- If you prefer to work on a single subproject:
  - Navigate to the subproject directory, set up a virtual environment, install dependencies, and run pytest in its tests directory.

Code quality
- Run linters and basic checks where applicable (flake8, mypy) per subproject guidelines.
- Include tests with meaningful coverage for any new feature or bug fix.

CI and PRs
- This repository uses a root-level test runner and GitHub Actions workflow to validate changes across subprojects.
- PRs should include a description of the changes and impact across subprojects, not just a single subproject's tests.

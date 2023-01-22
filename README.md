# commits-counter

Scans the provided directory and all its subdirectories for git repositories.
For each repository, counts the number of commits made by the provided author on the `main` branch between the provided start and end date.

## Setup

```bash
pip install -r requirements.txt
```

## Usage

See `./commits_counter.py --help`

Example usage:
```bash
./git_commits_scanner.py ~/projects/ 'Jon' -b '2022-03-20' -e '2023-01-20'
```

Example output:
```
Total commits by Jon: 102
Commits in /Users/Jon/projects/ppp: 73 (71.57%)
Commits in /Users/Jon/projects/aaa: 11 (10.78%)
Commits in /Users/Jon/projects/bbb: 10 (9.80%)
Commits in /Users/Jon/projects/zzz: 5 (4.90%)
Commits in /Users/Jon/projects/fff: 2 (1.96%)
Commits in /Users/Jon/projects/ddd: 1 (0.98%)
```
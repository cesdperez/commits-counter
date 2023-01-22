#!/usr/bin/env python3

import fire
import os
import subprocess


def get_commit_count(directory, author, begin_date=None, end_date=None):
    commit_count = 0
    repo_commits = {}
    try:
        subprocess.check_output(["git", "--version"])
    except OSError as e:
        print("Error: git is not installed.")
        return
    for root, dirs, files in os.walk(directory):
        if '.git' in dirs:
            os.chdir(root)
            command = f"git log main --author={author} --pretty=format:'%h'"
            if begin_date:
                command += f" --since={begin_date}"
            if end_date:
                command += f" --until={end_date}"
            try:
                output = subprocess.check_output(
                    command, shell=True, stderr=subprocess.DEVNULL)
                if (len(output) == 0):
                    repo_commit_count = 0
                else:
                    repo_commit_count = len(output.strip().split(b'\n'))
                commit_count += repo_commit_count
                repo_commits[root] = repo_commit_count
            except subprocess.CalledProcessError as e:
                pass
            os.chdir('..')
    print(f"Total commits by {author}: {commit_count}")
    sorted_repo_commits = sorted(
        repo_commits.items(), key=lambda x: x[1], reverse=True)
    for repo, commits in sorted_repo_commits:
        if commits > 0:
            percentage = (commits / commit_count) * 100
            print(f"Commits in {repo}: {commits} ({percentage:.2f}%)")


if __name__ == '__main__':
    fire.Fire(get_commit_count)

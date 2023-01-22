#!/usr/bin/env python3

import fire
import os
import subprocess


def get_commit_count(directory, author, exclude_dirs=[]):
    commit_count = 0
    repo_commits = {}
    try:
        subprocess.check_output(["git", "--version"])
    except OSError as e:
        print("Error: git is not installed.")
        return
    for root, dirs, files in os.walk(directory):
        if '.git' in dirs:
            should_exclude = any(
                exclude_dir in root for exclude_dir in exclude_dirs)
            if should_exclude:
                continue
            os.chdir(root)
            command = f"git log --author={author} --pretty=format:'%h'"
            try:
                output = subprocess.check_output(
                    command, shell=True, stderr=subprocess.DEVNULL)
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
            print(f"Commits in {repo}: {commits}")


if __name__ == '__main__':
    fire.Fire(get_commit_count)

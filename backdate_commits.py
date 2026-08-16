import os
import subprocess
import datetime
import random

# Target repository path
REPO_PATH = r"c:\Users\KIIT0001\Desktop\github"
LOG_FILE_PATH = os.path.join(REPO_PATH, "activity.log")

start_date = datetime.date(2026, 5, 15)
end_date = datetime.date(2026, 8, 16) # Today's date

current_date = start_date
total_commits = 0

# Random commit messages list to make it look realistic
commit_messages = [
    "Update project configuration and dependencies",
    "Refactor core module utilities",
    "Improve logging formatting and output",
    "Optimize internal caching mechanism",
    "Fix minor typos and wording in documentation",
    "Update testing harness and mocks",
    "Clean up unused variables and imports",
    "Add minor error handling to helpers",
    "Update local build workflow parameters",
    "Fix minor formatting in readme metrics",
    "Tweak scheduler interval values",
    "Synchronize repository activity log"
]

while current_date <= end_date:
    # 75% chance of activity on any given day
    if random.random() < 0.75:
        # Generate 1 to 4 commits
        num_commits = random.randint(1, 4)
        for i in range(num_commits):
            # Generate random time between 9:00 AM and 8:00 PM
            hour = random.randint(9, 20)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            
            commit_time = datetime.datetime.combine(current_date, datetime.time(hour, minute, second))
            iso_format = commit_time.isoformat() + "+05:30" # Match user's timezone +05:30
            
            # Write to log file
            with open(LOG_FILE_PATH, "a") as f:
                f.write(f"Activity entry on {iso_format} - commit {i+1}\n")
            
            # Set environment variables for backdating
            env = os.environ.copy()
            env["GIT_AUTHOR_DATE"] = iso_format
            env["GIT_COMMITTER_DATE"] = iso_format
            
            # Git add
            subprocess.run(["git", "add", "activity.log"], cwd=REPO_PATH, check=True)
            
            # Git commit
            msg = random.choice(commit_messages)
            subprocess.run(["git", "commit", "-m", msg], cwd=REPO_PATH, env=env, check=True)
            total_commits += 1
            
    current_date += datetime.timedelta(days=1)

print(f"Successfully generated {total_commits} commits from {start_date} to {end_date}!")

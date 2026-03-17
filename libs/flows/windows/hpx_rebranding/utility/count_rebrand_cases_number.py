import os
import re
from collections import defaultdict

# Rebrand analytics folder
TARGET_DIR = r'../../../../../tests/windows/hpx_rebranding/windows/analytics'
CASE_PATTERN = re.compile(r'C\d{8,}')

# Record the frequency of each case where it appears.
case_info = defaultdict(lambda: {"count": 0, "files": set()})

for root, _, files in os.walk(TARGET_DIR):
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                found = CASE_PATTERN.findall(content)
                for cid in found:
                    case_info[cid]["count"] += 1
                    case_info[cid]["files"].add(file_path)

print(f"total unique cases: {len(case_info)}")
print(f"total occurrences (including duplicates): {sum(info['count'] for info in case_info.values())}")

# Check for duplicate cases
print("\nCases that appear more than once:")
for cid, info in case_info.items():
    if info["count"] > 1:
        print(f"{cid}: {info['count']} times")
        

# Rebrand functional folder
TARGET_DIR = r'../../../../../tests/windows/hpx_rebranding/windows'
CASE_PATTERN = re.compile(r'C\d{8,}')

# Record the frequency of each case where it appears.
case_info = defaultdict(lambda: {"count": 0, "files": set()})

for root, dirs, files in os.walk(TARGET_DIR):
    # Exclude analytics folder
    if 'analytics' in dirs:
        dirs.remove('analytics')
    
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                found = CASE_PATTERN.findall(content)
                for cid in found:
                    case_info[cid]["count"] += 1
                    case_info[cid]["files"].add(file_path)

print(f"total unique cases: {len(case_info)}")
print(f"total occurrences (including duplicates): {sum(info['count'] for info in case_info.values())}")

# Check for duplicate cases
print("\nCases that appear more than once:")
for cid, info in case_info.items():
    if info["count"] > 1:
        print(f"{cid}: {info['count']} times")        

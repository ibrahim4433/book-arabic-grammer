import re
import sys

def normalize(text):
    return re.sub(r'[^\u0600-\u06FF]', '', text)

def get_trigrams(text):
    norm = normalize(text)
    return set(norm[i:i+3] for i in range(len(norm)-2))

def trigram_sim(t1, t2):
    if not t1 or not t2: return 0
    return len(t1.intersection(t2)) / max(len(t1), len(t2))

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.readlines()

out_lines = read_file('output.txt')
# Re-read the ORIGINAL raw_001 without our bad page markers
# Wait, the current raw_001.txt has page markers from our last attempt!
# I need to strip them out first to get the clean original file.
raw_lines_dirty = read_file('system-workspace/text-data/raw/raw_001.txt')
raw_lines = [l for l in raw_lines_dirty if not re.match(r'^\s*---\s*Page\s+\d+\s*---\s*', l)]

print(f"Original raw lines: {len(raw_lines)}")
print(f"Output lines: {len(out_lines)}")

out_trigrams = [get_trigrams(l) for l in out_lines]
raw_trigrams = [get_trigrams(l) for l in raw_lines]

# DP Alignment
# Since matrices of 9000x9000 are 81M elements, we can keep only 2 rows in memory for space,
# but we need the path!
# 81M integers in python is ~600MB, perfectly fine.
# We will use a banded DP to save memory and time.
W = 600 # band width
N = len(out_lines)
M = len(raw_lines)

# dp[i][j] stores (score, prev_j)
# since python lists of lists are slow, we can just use flat lists or dictionaries,
# or we can use the fact that we only need to map out_lines to raw_lines.
# Let's map each line of output.txt to a line in raw_001.txt greedily but with lookahead?
# A simpler DP:
dp = [{} for _ in range(N)]

# Initialize
dp[0][0] = (trigram_sim(out_trigrams[0], raw_trigrams[0]), -1)

for i in range(N):
    if i % 1000 == 0:
        print(f"Aligning line {i}/{N}")
    
    # expected j
    ej = int(i * M / N)
    start_j = max(0, ej - W)
    end_j = min(M, ej + W)
    
    for j in range(start_j, end_j):
        sim = trigram_sim(out_trigrams[i], raw_trigrams[j])
        
        # we can come from (i-1, j), (i, j-1), (i-1, j-1)
        best_score = -1
        best_prev_j = -1
        
        # from i-1, j-1
        if i > 0 and (j-1) in dp[i-1]:
            score = dp[i-1][j-1][0] + sim
            if score > best_score:
                best_score = score
                best_prev_j = j-1
                
        # from i-1, j (deletion in raw)
        if i > 0 and j in dp[i-1]:
            score = dp[i-1][j][0]
            if score > best_score:
                best_score = score
                best_prev_j = j
                
        # from i, j-1 (insertion in raw)
        if j-1 in dp[i]:
            score = dp[i][j-1][0]
            if score > best_score:
                best_score = score
                best_prev_j = j-1
                
        if i == 0 and j == 0:
            pass # already initialized
        else:
            dp[i][j] = (best_score, best_prev_j)

print("Backtracking...")
# Find best end j
best_end_j = -1
best_end_score = -1
for j in dp[N-1]:
    if dp[N-1][j][0] > best_end_score:
        best_end_score = dp[N-1][j][0]
        best_end_j = j

# Backtrack
mapping = {} # output_idx -> raw_idx
curr_j = best_end_j
for i in range(N-1, -1, -1):
    mapping[i] = curr_j
    if curr_j in dp[i]:
        curr_j = dp[i][curr_j][1]

# Now we find where page markers should go
page_inserts = {}
for i, line in enumerate(out_lines):
    m = re.match(r'^---\s*Page\s+(\d+)\s*---', line.strip())
    if m:
        page_num = int(m.group(1))
        # The page marker at line i in output.txt
        # It should be placed BEFORE the line in raw_001.txt that corresponds to the first content line AFTER i
        # Let's find the first line after i that has a strong match
        mapped_j = -1
        for k in range(i+1, min(N, i+15)):
            if mapping[k] != -1:
                # check if it's a real match
                sim = trigram_sim(out_trigrams[k], raw_trigrams[mapping[k]])
                if sim > 0.1:
                    mapped_j = mapping[k]
                    break
        
        if mapped_j != -1:
            line_num = mapped_j
            if line_num not in page_inserts:
                page_inserts[line_num] = []
            page_inserts[line_num].append(page_num)
        else:
            print(f"Warning: Could not confidently place Page {page_num}")

new_raw_lines = []
for i, line in enumerate(raw_lines):
    if i in page_inserts:
        for pnum in page_inserts[i]:
            new_raw_lines.append(f"\n--- Page {pnum} ---\n\n")
    new_raw_lines.append(line)

with open('system-workspace/text-data/raw/raw_001.txt', 'w', encoding='utf-8') as f:
    f.writelines(new_raw_lines)
print(f"Inserted {sum(len(v) for v in page_inserts.values())} page markers exactly.")

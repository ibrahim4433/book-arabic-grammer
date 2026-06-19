import requests
import json
import os
import time

def merge_all_open_prs():
    print("Fetching GitHub token...")
    try:
        with open("secrets/Github_Token.txt") as f:
            token = f.read().strip()
    except Exception as e:
        print(f"❌ Error reading token: {e}")
        return

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    owner = "ibrahim4433"
    repo = "book-arabic-grammer"
    
    print(f"Fetching open PRs for {owner}/{repo}...")
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls?state=open&per_page=100"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        prs = response.json()
    except Exception as e:
        print(f"❌ Failed to fetch PRs: {e}")
        return

    if not prs:
        print("✅ No open PRs found.")
        return

    print(f"Found {len(prs)} open PRs. Starting merge process...")

    success_count = 0
    fail_count = 0

    for pr in prs:
        pr_num = pr['number']
        pr_title = pr['title']
        
        print(f"\nAttempting to merge PR #{pr_num}: {pr_title}")
        merge_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_num}/merge"
        
        data = {
            "commit_title": f"Auto-Merge PR #{pr_num}",
            "merge_method": "squash"
        }
        
        try:
            resp = requests.put(merge_url, headers=headers, json=data)
            if resp.status_code == 200:
                print(f"✅ Successfully merged PR #{pr_num}.")
                success_count += 1
                
                # Delete the branch
                branch_name = pr['head']['ref']
                delete_url = f"https://api.github.com/repos/{owner}/{repo}/git/refs/heads/{branch_name}"
                del_resp = requests.delete(delete_url, headers=headers)
                if del_resp.status_code == 204:
                    print(f"   🗑️ Deleted branch {branch_name}")
            else:
                print(f"❌ Failed to merge PR #{pr_num}. Status Code: {resp.status_code}")
                try:
                    print(f"   Reason: {resp.json().get('message')}")
                except:
                    pass
                fail_count += 1
        except Exception as e:
            print(f"❌ Exception merging PR #{pr_num}: {e}")
            fail_count += 1
            
        time.sleep(1) # Sleep slightly to avoid API rate limits

    print("\n" + "="*40)
    print("Merge Process Complete!")
    print(f"Successfully Merged: {success_count}")
    print(f"Failed to Merge: {fail_count}")

if __name__ == "__main__":
    merge_all_open_prs()

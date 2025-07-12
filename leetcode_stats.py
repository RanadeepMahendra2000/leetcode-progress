import time
import requests

LEETCODE_USERNAME = 'ranadeep_mahendra2426'

def fetch_leetcode_data(username):
    url = f'https://leetcode-stats-api.herokuapp.com/{username}'
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()

def update_readme(data):
    ts = int(time.time())

    with open('README.md', 'w') as f:
        f.write("# 👋 Hi, I'm Ranadeep Mahendra!\n\n")
        f.write("## 🏆 My LeetCode Progress\n\n")

        # dynamic, cache-busted badges:
        f.write(
            f"![LeetCode Questions Solved]"
            f"(https://img.shields.io/badge/Solved-{data['totalSolved']}/{data['totalQuestions']}-blue"
            f"?cache={ts}) "
        )
        f.write(
            f"![LeetCode Easy]"
            f"(https://img.shields.io/badge/Easy-{data['easySolved']}/{data['totalEasy']}-brightgreen"
            f"?cache={ts}) "
        )
        f.write(
            f"![LeetCode Medium]"
            f"(https://img.shields.io/badge/Medium-{data['mediumSolved']}/{data['totalMedium']}-orange"
            f"?cache={ts}) "
        )
        f.write(
            f"![LeetCode Hard]"
            f"(https://img.shields.io/badge/Hard-{data['hardSolved']}/{data['totalHard']}-red"
            f"?cache={ts})\n\n"
        )

        f.write("### 📊 LeetCode Activity Graph\n\n")
        f.write(
            f"![LeetCode Activity Graph]"
            f"(https://leetcard.jacoblin.cool/{LEETCODE_USERNAME}"
            f"?theme=dark&font=Karma&ext=heatmap&cache={ts})\n"
        )

if __name__ == "__main__":
    stats = fetch_leetcode_data(LEETCODE_USERNAME)
    update_readme(stats)

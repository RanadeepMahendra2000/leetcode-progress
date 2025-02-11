import requests

LEETCODE_USERNAME = 'ranadeep_mahendra2426'  # Replace with your actual LeetCode username

def fetch_leetcode_data(username):
    url = f'https://leetcode-stats-api.herokuapp.com/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data")
        return None

def update_readme(data):
    with open('README.md', 'w') as f:
        f.write(f"# LeetCode Progress 📈\n")
        f.write(f"**Username:** {LEETCODE_USERNAME}\n\n")
        f.write(f"**Total Solved:** {data['totalSolved']} / {data['totalQuestions']}\n\n")
        f.write(f"**Easy:** {data['easySolved']} / {data['totalEasy']}\n")
        f.write(f"**Medium:** {data['mediumSolved']} / {data['totalMedium']}\n")
        f.write(f"**Hard:** {data['hardSolved']} / {data['totalHard']}\n")

if __name__ == "__main__":
    data = fetch_leetcode_data(LEETCODE_USERNAME)
    if data:
        update_readme(data)

import getpass
from github import Github


# Ask the user to create a personal access token on the GitHub website
print("Please create a personal access token on the GitHub website:")
print("  1. Go to https://github.com/settings/tokens")
print("  2. Click 'Generate new token'")
print("  3. Give the token a description called 'MineKhan Desktop Access'")
print("  4. Select the 'repo' scope")
print("  5. Click 'Generate token'")
print("  6. Copy the token and paste it below")
access_token = getpass.getpass("Enter your GitHub access token: ")

g = Github(access_token)

# Save the access token to a file
with open("access_token.pem", "w") as f:
    f.write(access_token)

print("Access token saved to access_token.pem")

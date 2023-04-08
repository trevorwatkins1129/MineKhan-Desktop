import os
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton, QVBoxLayout, QWidget, QTextBrowser
from github import Github

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        try:
            with open('access_token.pem', 'r') as key:
                access_token = key.read()
        except:
            print("Please run setup.py")
            exit()

        repo_name = 'Willard21/MineKhan'

        # Initialize a Github instance with your access token
        g = Github(access_token)

        # Get the repository object
        repo = g.get_repo(repo_name)

        # Get the first commit in the repository
        first_commit = repo.get_commits().reversed[0]

        # Get all the commits in the repository since the date of the first commit
        commits = repo.get_commits(since=first_commit.commit.author.date)

        # Create a QPushButton widget for playing the selected version
        self.play_button = QPushButton('Play', self)
        self.play_button.clicked.connect(self.play_selected_version)

        # Create a QTextBrowser widget to display the commit messages
        self.text_browser = QTextBrowser(self)

        # Create a QVBoxLayout to hold the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.play_button)
        layout.addWidget(self.text_browser)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Set the text of the QTextBrowser widget to the messages of all the commits
        commit_messages = '\n\n'.join([commit.commit.message for commit in commits])
        self.text_browser.setText(commit_messages)

    def play_selected_version(self):

        # Check is version is installed
        with open ('./options/options.json', 'r') as file:
            options = json.load(file)
            user = options['username'] + "@" + options["hostname"]
        userhash = "".join(chr(ord(c) + 47) if 33 <= ord(c) <= 126 else c for c in user)
        print(userhash)
        
        os.system(f"python3 browser.py https://www.willard.fun/minekhan")

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


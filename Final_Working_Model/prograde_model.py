from prograde_core import analyze_repository

class ProGrade:
    def __init__(self, name="ProGrade"):
        self.name = name

    def analyze(self, repo_path):
        return analyze_repository(repo_path)

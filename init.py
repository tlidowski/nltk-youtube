import subprocess
if __name__ == "__main__":
    subprocess.run(["pip", "install", "--upgrade", "google-api-python-client"])
    subprocess.run(["pip", "install", "--upgrade", "google-auth-oauthlib", "google-auth-httplib2"])
    subprocess.run(["pip", "install", "python-dotenv"])
    subprocess.run(["pip", "install", "-q", "transformers"])
    subprocess.run(["pip3", "install", "emoji==0.6.0"])
    subprocess.run(["pip", "install", "reportlab"])
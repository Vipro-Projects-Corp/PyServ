import requests

def run_server():
  """Runs the server.py file on the specified website."""
  website = input("Enter the website: ")
  url = "https://" + website + "/server.py"
  response = requests.get(url)
  if response.status_code == 200:
    code = response.content
    exec(code)
  else:
    print('Error: The website "'+ website + '" either does not exist, or does not run a pythonserver. Maybe there is a typo?')

if __name__ == "__main__":
  run_server()

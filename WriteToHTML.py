from bs4 import BeautifulSoup

# Read the HTML file
with open("index.html", "r") as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Find the input field by its name attribute
input_field = soup.find("input", {"name": "inp_name"})

# Update the value of the input field
input_field["value"] = ""

# Save the modified HTML content
with open("index.html", "w") as file:
    file.write(str(soup))

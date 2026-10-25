import requests

url = "https://gsom.spbu.ru/en/"
response = requests.get(url)
html = str(response.content)

print("Status:", response.status_code)
print("PNG count:", html.count(".png"))

position = html.find(".png")

if position != -1:
	start = html.rfind('"', 0, position)
	path = html[start + 1:position + 4]
	image_url = "https://gsom.spbu.ru" + path
	
	print("Image URL:", image_url)

	image = requests.get(image_url)

	with open("first_image.png", "wb") as file:
		file.write(image.content)

	print("Image saved:", image.status_code)

	


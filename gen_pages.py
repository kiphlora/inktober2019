import os
import json

def mkdir(path):
	if not os.path.isdir(path):
		os.mkdir(path)


jpegs = list(os.walk("drawings/")).pop()[2]
jpegs = [x.split(".")[0] for x in jpegs if '.jpg' in x]
print(jpegs)
mkdir('theprocess')
for drawing in jpegs:
	mkdir(f'theprocess/{drawing}')

prompt_num, prompt_name = jpegs[0].split("_")


def makehtml(prompt_num, prompt_name):
	# create basic html pages for the process
	html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Process for Prompt {prompt_num} - {prompt_name.capitalize()}</title>

<link href="https://fonts.googleapis.com/css?family=Dosis:200" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="../../kiphlora_website_styling/css/project-theme.css">
<link rel="stylesheet" type="text/css" href="../../kiphlora_website_styling/css/page-style.css">
<link rel="stylesheet" type="text/css" href="../../kiphlora_website_styling/font-awesome/css/font-awesome.min.css">

<style>

figure {{
	padding: 15px;
	/*border: 1px solid #000;*/
	margin: 20px;
	box-shadow: 0px 0px 8px 5px #bbb;
}}

</style>
</head>
<body>
<div class="container">
<header class="hero-header">
	<div class="my-name">Process for Prompt {prompt_num} - {prompt_name.capitalize()}</div>
	<div class="nav">
		<!-- <a href="about/index.html"><div class="about-nav"></div></a> -->
		<a href="http://www.kiphlora.com"><div class="portfolio-nav"><i class="fa fa-home" aria-hidden="true"></i></div></a>
	</div>
</header>

<div class="hero-content-wrapper">
	<div class="intro-content">
	<figure>
		<img src="../../drawings/{prompt_num}_{prompt_name}.jpg" alt="Prompt {prompt_num} - {prompt_name.capitalize()}">
		<figcaption>{int(prompt_num)}. {prompt_name.capitalize()}</figcaption>
	</figure>
	</div>
<footer class="hero-footer">
	<div class="footer-info">
	<a href="https://github.com/kiphlora/inktober2019"><div><i class="fa fa-github" aria-hidden="true"></i>Inktober 2019</div></a>
	<a href="mailto:kiphlora@gmail.com" target="_top"><div><i class="fa fa-envelope" aria-hidden="true"></i>kiphlora@gmail.com</div></a>
	<p>&copy 2017-2020 Brett Moran</p>
</div>
</footer>
</div>
</body>
</html>
'''
	return html

htmls = [makehtml(*x.split("_")) for x in jpegs]
for i,html in enumerate(htmls):
	print(jpegs[i])
	print(html)
	with open(f"theprocess/{jpegs[i]}/index.html", 'w') as f:
		f.write(html)






def make_prompt_links(prompt_num, prompt_name):
	link = f'''
		<a href="theprocess/{prompt_num}_{prompt_name}/index.html">
		<figure>
			<img src="drawings/{prompt_num}_{prompt_name}.jpg" alt="Prompt {prompt_num} - {prompt_name.capitalize()}">
			<figcaption>{int(prompt_num)}. {prompt_name.capitalize()}</figcaption>
		</figure>
		</a>'''
	return link


links = [make_prompt_links(*x.split("_")) for x in jpegs]
page_links = "\n".join(links)
	




main_page = f'''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Inktober 2019</title>

<link href="https://fonts.googleapis.com/css?family=Dosis:200" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="css/drawing_theme.css">
<link rel="stylesheet" type="text/css" href="kiphlora_website_styling/css/project-theme.css">
<link rel="stylesheet" type="text/css" href="kiphlora_website_styling/css/page-style.css">
<link rel="stylesheet" type="text/css" href="kiphlora_website_styling/font-awesome/css/font-awesome.min.css">

<style>
</style>

</head>

<body>
<div class="container">
<header class="hero-header">
	<div class="my-name">Inktober 2019</div>
	<div class="nav">
		<!-- <a href="about/index.html"><div class="about-nav"></div></a> -->
		<a href="https://www.kiphlora.com"><div class="portfolio-nav"><i class="fa fa-home" aria-hidden="true"></i></div></a>
	</div>
</header>

<div class="hero-content-wrapper">
	<div class="intro-content">

		<a href="https://inktober.com/" class='prompt-list'>
		<figure>
			<img src="drawings/inktober_prompt_list_2019.png" alt="Inktober 2019 Official Prompt List">
			<figcaption>Inktober 2019 Official Prompt List</figcaption>
		</figure>
		</a>

		<div class="drawing-flex">
		{page_links}
		</div>
	</div>
</div>

<footer class="hero-footer">
	<div class="footer-info">
	<a href="https://github.com/kiphlora/inktober2019"><div><i class="fa fa-github" aria-hidden="true"></i>Inktober 2019</div></a>
	<a href="mailto:kiphlora@gmail.com" target="_top"><div><i class="fa fa-envelope" aria-hidden="true"></i>kiphlora@gmail.com</div></a>
	<p>&copy 2017-2020 Brett Moran</p>
	</div>
</footer>

</div>

</body>
</html>
'''

print(main_page)

with open("index.html", "w") as f:
	f.write(main_page)
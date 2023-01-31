import os 
import sys

	
def get_project_name() -> str:
	"""
	This function format the project name.

	Returns: 
		str: project name
	"""
	project_name  = sys.argv[1]
	not_allowed = ["/","\\","<",">","|","*","?",'"',":"]
	for proiben_chr in not_allowed:
		if proiben_chr in project_name:
			print(proiben_chr, "cannot be in proejct name but the project is  still created under the name: default-name.")
			project_name = "default-name" 
			return project_name
		else: 
			continue
	return project_name
	
def create_project_folders(path: str, project_name: str) -> None:
	"""
	This function create images scripts and styles folders.

	Args:
		path(str): the path to save the project to.
		project_name(str): the project name.

	"""
	if sys.platform =="win32":
		os.system("mkdir " + path + "\\" + project_name)
		os.system("mkdir " + path + "\\" + project_name + "\\" + "images")
		os.system("mkdir " + path + "\\" + project_name + "\\" + "scripts")
		os.system("mkdir " + path + "\\" + project_name + "\\" + "styles")
		print("project saved to: " + path + "\\" + project_name + "\\" )
	else:
		os.system("mkdir " + path +"/" +project_name)
		os.system("mkdir " + path +"/" +project_name + "/" + "images")
		os.system("mkdir " + path +"/" +project_name + "/" + "scripts")
		os.system("mkdir " + path +"/" +project_name + "/" + "styles")
		print("project saved to: "  + path + "/" + project_name + "/" )

def create_project_files(path: str, project_name: str, template: str) -> None:
	"""
	This function create the site-files like index.html scripts.js and styles.css.

	Args:
		path(str): the path to save the project to.
		project_name(str): the project name.
		template(str): the project template.
	
	"""
	if template == "blank":
		from templates import html_blank, java_script_blank, css_blank
		html = html_blank
		java_script = java_script_blank
		css = css_blank
	else:
		from templates import html, java_script, css
	
	if sys.platform == "win32":
		with open(path + "\\" + project_name + "\\" + "index.html" ,"w")as index_html:
			index_html.write(html)

		with open(path + "\\" + project_name + "\\" + "styles" + "\\" + "style.css" ,"w")as styles_css:
			styles_css.write(css)

		with open(path + "\\" + project_name + "\\" + "scripts" + "\\" + "script.js","w")as styles_css:
			styles_css.write(java_script)
		
	else:
		with open(path + "/" + project_name + "/" + "index.html","w")as index_html:
			index_html.write(html)
		with open(path + "/" + project_name + "/" + "styles" + "/" + "style.css","w")as styles_css:
			styles_css.write(css)
		with open(path + "/" + project_name+ "/" + "scripts" + "/" + "script.js","w")as styles_css:
			styles_css.write(java_script)
	
if __name__=="__main__":
	if len(sys.argv) == 3:
		project_name = get_project_name()
		create_project_folders(path=sys.argv[2],project_name=project_name)
		create_project_files(path=sys.argv[2],project_name=project_name,template="blank")
	elif len(sys.argv) == 4:
		if sys.argv[-1].lower() in ["color","blank"]:
			project_name = get_project_name()
			create_project_folders(path=sys.argv[2],project_name=project_name)
			create_project_files(path=sys.argv[2] ,project_name=project_name,template=sys.argv[-1].lower())
		else:
			print("no such template: " + sys.argv[-1] )
			print("templates: " + "color, blank")
	else:
		print("could not create project.")
		print("a command should look like that:"  + "python html_maker.py project_name /path/to/save/to  color/blank")
		
	
		

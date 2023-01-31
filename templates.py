###############################################################################################################
#                                       Change Background Color Page                                          #
###############################################################################################################
html = """<!DOCTYPE html>
<html>
<head>
\t<link rel="stylesheet" href="styles/style.css">
\t<script src="scripts/script.js"></script>
\t<title>structure</title>
</head>
<body>
\t<h1>simple site structure</h1>
\t<hr>
\t<p class="paragraph-1">
\t\tThis site structure has a main folder that contain three folders that holds diffrent assets like images scripts or styles.<br>
\t\tThe main html file come from project-name/index.html<br>
\t\tThe images can come from project-name/images/image-name.png but on this example the image come from a web resource.<br>
\t\tThe page style come from  project-name/stryle/style.css.<br>
\t\tTo see the script from project-name/scripts/script.js get excuted click on the button below.
\t</p>
\t<div class="group">
\t\t<div class="left-image"><img class="image-1" src="https://www.gstatic.com/webp/gallery3/1.png"></div>
\t\t<div class="script-button"><br><br><br><br><br><br><br><br><button class="btn" onclick="onClicks()">change background color</button></div>
\t\t<div class="right-image"><img class="image-2" src="https://www.gstatic.com/webp/gallery3/1.png"></div>
\t</div>
\t<hr>
</body>
</html>
"""
css ="""body {
		background-color: #fa7c52;
	}
hr {
border: 4px solid black;
}
h1 {
  color: white;
  font-family: courier;
  font-size: 300%;
  text-align: center;
}
.paragraph-1 {
  color: white;
  font-family: courier;
  font-size: 160%;
  text-align: left;
}
.left-image {
  float: left;
  width: 33.33%;
  text-align:left;
}
.script-button{
  float: left;
  width: 33.33%;
  text-align:center;
}
.right-image {
  float: left;
  width: 33.33%;
  text-align:right;
}
.group:after {
  content: "";
  display: table;
  clear: both;
}	
img {
	width:335px;
	height:335px	
}
.image-1 {
  	transform: scaleX(-1);
}
.btn {
  transition-duration: 0.2s;
  background-color: transparent;
  color: white;
  text-align: center;
  border:none;
  font-family: courier;
  font-size: 32px;
}
.btn:hover {
  background-color: black;
  color:white;
}
"""
java_script ='''var flag = 0;
function onClicks() {
	if (flag == 0){		
		document.body.style.backgroundColor="#c765c2";		
		flag=1;
	}else{		
		document.body.style.backgroundColor="#fa7c52";
		flag=0;		
	}
}

'''


###############################################################################################################
#                                       Blank Page                                                            #
###############################################################################################################
html_blank = """<!DOCTYPE html>
<html>
<head>
\t<link rel="stylesheet" href="styles/style.css">
\t<script src="scripts/script.js"></script>
\t<title>blank</title>
</head>
<body>
</body>
</html>
"""
css_blank = """
body {
		background-color: #fa7c52;
	}
"""
java_script_blank = """"""
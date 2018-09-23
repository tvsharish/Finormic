import json
f = open( "package.json" , "rb" )
d = json.load(f)
f.close()
with open("requirements.txt", "w+") as fb:
     for i,j in zip(d["dependencies"].keys(), d["dependencies"].values()):
         line = "{}=={}\n".format(i, j.strip("^"))
         fb.writelines(line)
fb.close()        
           
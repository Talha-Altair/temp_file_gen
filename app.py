def fetch_flask():
    f=open("data_flask.txt", "r")
    if f.mode == 'r':
        contents =f.read()
    g= open("Tact_Template.py","w+")
    g.write(contents)

def fetch_html():
    f=open("data_html.txt", "r")
    if f.mode == 'r':
        contents =f.read()
    g= open("Tact_Template.html","w+")
    g.write(contents)

print("Greetings!! ")
print("Pls Specify Which File Template you would like to generate")
print("\n1.Flask Template")
print("\n2.HTML Template\n")

s=int(input())

if s==1:
    fetch_flask()
else:
    if s==2:
        fetch_html()
    else:
        print("Please Enter Valid Option")





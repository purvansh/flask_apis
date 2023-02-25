from flask import Flask ,render_template,request
import json
app = Flask(__name__)

listdata = [
{
    "name":"purvansh",
    "age":22,
    "id":1,
    "h":True
    },
    {
    "name":"ram",
    "age":21,
     "h":True,
    "id":2
    }
]



@app.route('/')
def index():
    return render_template('index.html',listdata = listdata)

@app.route('/data')
def data():
    return json.dumps(listdata)

@app.route('/data/<int:id>')
def data_for_id(id):
    for i in listdata:
        if i.get("id") == id:
            return i
    # return json.dumps(listdata)

@app.route('/dataadd',methods=['POST'])
def data_for_name():
    if request.method == 'POST':
        print(request.data)
        data = json.loads(request.data)
        name = data.get("name")
        age = data.get("age")
        h = data.get("h")
        nedata = {"name":name,"age":age,"h":h,"id":len(listdata)}
        listdata.append(nedata)
        return json.dumps(nedata)
        

if __name__ =="__main__":
    app.run(debug=True,host="0.0.0.0",port = 80)



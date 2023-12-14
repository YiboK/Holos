from flask import Flask, request
import service
import json

db = None

app = Flask(__name__)
 
@app.route('/insert',methods=['POST'])
def insertUserData():
    json_data = request.get_json()
    db.insert(json_data["subject"],json_data["topic"],json_data["id"],int(json_data["duration"]))
    # print(json_data)
    return 'Received JSON data: ' + str(json_data)

@app.route('/topn',methods=['GET'])
def getTopN():
    n = int(request.args.get('n', 3))
    return "Top N subjects: " + str(db.getTopNSubjects(n))

@app.route('/topntopic',methods=['GET'])
def getTopNTopic():
    n = int(request.args.get('n', 3))
    subject = request.args.get('subject', "")
    return "Top N topics in " + subject +  ": " + str(db.getTopNTopicsBySubject(n,subject))

# main driver function
if __name__ == '__main__':
    #TODO: init cassadra
    db = service.CassDB()
    app.run(debug=True, port=8000)
from flask import Flask, render_template, request
import json
import random

app = Flask(__name__)

with open("data/answers.json", 'r', encoding="utf8") as jsonfile:
	questions_dict = json.load(jsonfile)

list_of_questions = [questions_dict[key]["question"] for key in questions_dict.keys()]

print(list_of_questions)

questions_to_id_dict = dict()
counter = 0
for question in list_of_questions:
	questions_to_id_dict[question] = counter
	counter += 1

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/get_questions", methods=["GET", "POST"])
def get_questions():
	number_of_questions = int(request.args.get("n"))
	print(number_of_questions)
	return_dict = {}
	counter = 0

	if number_of_questions is not None and number_of_questions < len(list_of_questions):
		random.shuffle(list_of_questions)
		for item in list_of_questions:
			return_dict[counter] = {"question": item}
			counter += 1
			if counter >= number_of_questions:
				break

	else:
		for item in list_of_questions:
			return_dict[counter] = {"question":item}
			counter += 1

	return json.dumps(return_dict)

@app.route("/ask", methods=["GET", "POST"])
def ask():
	question = request.args.get("resp").replace("%20",' ')
	question_id = questions_to_id_dict[question]
	print(questions_dict[str(question_id)])
	return json.dumps(questions_dict[str(question_id)])

if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True)
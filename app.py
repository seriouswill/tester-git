from flask import Flask, render_template, request
from chatbot import predict_class, get_response, intents
from time import sleep

# chatbot is the name of our python chatbot


app = Flask(__name__)
app.config['SECRET__KEY'] = 'a_very_secretive_key_123456789'
answer_list = []            # This is an optional list to 
                            #   populate with our chatbot 									
                            # responses
delay = sleep(0.03)

@app.route("/")
def home():
    global answer_list
    answer_list.clear()
    return render_template("index.html")


@app.route("/chatbot", methods=["GET", "POST"])
def chatbot():
    global answer_list, delay
    if request.method == "POST":
        message = request.form['message']
        ints = predict_class(message)
        response = get_response(ints, intents)
        answer_list.append(response)
        print(answer_list)                      # To see the correct responses in the terminal
        if len(answer_list) > 4:                # Populating 
            answer_list.remove(answer_list[0])
        return render_template("chatbot.html", message=message, answer_list=answer_list, delay=delay)
    return render_template("chatbot.html", message="", answer_list=answer_list)


if __name__ == "__main__":
    app.run(debug=True)

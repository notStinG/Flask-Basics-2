from flask import Flask, render_template

app = Flask(__name__)

valid_animals = ["chicken", "panda"]

@app.route('/')
def index():
    return render_template('index.html')

info = {
    "chicken": "The chicken (Gallus domesticus) is a large and round short-winged bird, domesticated from the red junglefowl of Southeast Asia around 8,000 years ago. Most chickens are raised for food, providing meat and eggs; others are kept as pets or for cockfighting. Chickens are common and widespread domestic animals, with a total population of 23.7 billion as of 2018, and an annual production of more than 50 billion birds. A hen bred for laying can produce over 300 eggs per year. There are numerous cultural references to chickens in folklore, religion, and literature.",
    "panda": "The giant panda (Ailuropoda melanoleuca), also known as the panda bear or simply panda, is a bear species endemic to China. It is characterised by its black-and-white coat and rotund body. The name 'giant panda' is used to distinguish it from the distantly related red panda. Adult individuals average 100 to 115 kg (220 to 254 lb), and are typically 1.2 to 1.9 m (3 ft 11 in to 6 ft 3 in) long. The species is sexually dimorphic, as males are typically 10 to 20% larger. The fur is white, with black patches around the eyes, ears, legs and shoulders. A thumb is visible on the bear's forepaw, which helps in holding bamboo in place for feeding. Giant pandas have adapted larger molars and expanded temporal fossa to meet their dietary requirements."
}

@app.route('/<animal>')
def animal_info(animal):
    if animal in valid_animals:
        return render_template(f"{animal}.html")
    else:
        return render_template("index.html")

if __name__ == '__main__':
  app.run(debug=True, port=5000)

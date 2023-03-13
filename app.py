from flask import Flask, request, render_template
# from stories import story
from stories import story1, story2, story3, story4, story5, story6

app = Flask(__name__)
app.config['SECRET_KEY'] = "skey000"
app.config['DEBUG'] = True

@app.route('/home')
def home():
    stories = [story1, story2, story3, story4, story5, story6]
    return render_template('home.html', stories=stories)

# Single story form route. 
# @app.route('/form')
# def form():
#     # render the form template with the story prompts
#     return render_template('form.html', story=story)

# @app.route('/form/<int:story_id>')
# def form(story_id):
#     # get the correct story based on the story_id
#     stories = [story1, story2, story3, story4, story5, story6]
#     # my_story = next((s for s in stories if s.id == story_id), None)
#     my_story = next((s for s in stories if s.title == request.args.get("story_id")), None)
    
# @app.route('/form')
# def form():
#     stories = [story1, story2, story3, story4, story5, story6]
#     my_story = next((s for s in stories if s.title == request.args.get("story_id")), None)
#     return render_template('form.html', story=my_story)


#     # render the form template with the story prompts
#     return render_template('form.html', story=my_story)

@app.route('/form')
def form():
    if 'story_id' not in request.args:
        return "Error: Missing story ID parameter."
    
    story_id = int(request.args.get('story_id'))
    stories = [story1, story2, story3, story4, story5, story6]
    my_story = next((s for s in stories if s.id == story_id), None)
    if my_story is None:
        return "Error: Invalid story ID."
    
    return render_template('form.html', story=my_story)

# @app.route('/generate')
# def generate():
#     """Generate and show story from prompts.""" 
#     my_story = next((s for s in [story]), None)

#     answers = {prompt: request.args.get(prompt) for prompt in my_story.prompts}
#     text = my_story.generate(answers)

#     return render_template("story.html", story_text=text)

@app.route('/generate')
def generate():
    """Generate and show story from prompts."""
    story_id = request.args.get("story_id")
    stories = [story1, story2, story3, story4, story5, story6]
    my_story = next((s for s in stories if s.id == int(story_id)), None)

    answers = {prompt: request.args.get(prompt) for prompt in my_story.prompts}
    text = my_story.generate(answers)

    return render_template("story.html", story_text=text)


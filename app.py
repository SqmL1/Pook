from flask import Flask, render_template


'''
Small Web app of pigeons walking around
they should be interactable 
clicking on them should make them eat bread crumbs
'''

# TODO:
# Create a nice looking homepage:
#   1. appealing background
#
# Render pigeons standing still
#
#
# find/design sprites for the pigeon
#   1. Walking animation
#       a. step 1
#       b. setp 2
#   2. Peck 
#   3. Standing still
#



app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')





from flask import Flask,request, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', tab='Home | SD Reconnect')

#@app.route('/searchbar')
#def searchbar():
#    input = request.args.get('input')
 #   return f"{input} is not available now."

@app.route('/services')
def services():
    images = [
        {
            "link": "https://gcdnb.pbrd.co/images/Jv5w69X3UAxZ.png", "text": "Housing & Shelter", "icon_name": "housing"
        },
        {
            "link": "https://gcdnb.pbrd.co/images/FePB8qtITrXe.png", "text": "Employment & Jobs", "icon_name": "jobs"
        },
        {
            "link": "https://gcdnb.pbrd.co/images/IJbSYFvfTqEQ.png", "text": "Medical Aid", "icon_name": "medical"
        },
        {
            "link": "https://gcdnb.pbrd.co/images/U8WFLyuvOAZB.png", "text": "Social Services", "icon_name": "socserv"
        }
    ]
    return render_template('services.html', elements=images)


@app.route('/category/<category_name>')
def category_page(category_name):
    return render_template('index.html', tab="Category", category_name=category_name)






@app.route('/about')
def about():
    return render_template('index.html', tab='About This Website')

@app.route('/trends')
def trends():
    return render_template('index.html', tab='Trends')

@app.route('/contact')
def contact():
    return render_template('index.html', tab='Contact Us')




if __name__ == '__main__':
    app.run(port=5000,debug=True)


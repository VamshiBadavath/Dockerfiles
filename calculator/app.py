from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure random key

# Mock user data (you can replace this with database integration)
user = {
    'username': 'JohnDoe',
    'email': 'john.doe@example.com',
    'bio': 'This is my bio.'
}

@app.route('/')
def profile():
    return render_template('profile.html', username=user['username'], email=user['email'], bio=user['bio'])

@app.route('/update', methods=['POST'])
def update_profile():
    user['username'] = request.form['username']
    user['email'] = request.form['email']
    user['bio'] = request.form['bio']
    return render_template('profile.html', username=user['username'], email=user['email'], bio=user['bio'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

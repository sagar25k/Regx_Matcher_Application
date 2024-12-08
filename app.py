from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling regex matching
@app.route('/results', methods=['POST'])
def results():
    # Extract input data from the form
    test_string = request.form.get('test_string', '')
    regex_pattern = request.form.get('regex_pattern', '')

    matches = []
    try:
        # Perform regex matching
        matches = re.findall(regex_pattern, test_string)
    except re.error as e:
        # Handle invalid regex patterns
        matches = [f"Error in regex: {e}"]

    # Render the results on the same page
    return render_template('index.html', test_string=test_string, regex_pattern=regex_pattern, matches=matches)

# Route for email validation
@app.route('/validate_email', methods=['POST'])
def validate_email():
    # Extract email from the form
    email = request.form.get('email', '')

    # Regex pattern for email validation
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # Validate email using regex
    is_valid = re.match(email_regex, email) is not None
    message = "Valid email" if is_valid else "Invalid email"

    # Render the validation result
    return render_template('index.html', email=email, email_validation_message=message)

if __name__ == '__main__':
    app.run(debug=True)

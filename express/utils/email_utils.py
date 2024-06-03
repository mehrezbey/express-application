from express import mail
from flask_mail import Message 
from flask import url_for 

def send_reset_password_email(user):
    token = user.get_reset_token()
    msg = Message("Express | Password Reset Request",sender="noreply@express.com",recipients=[user.email])
    msg.html = f'''
    <html>
    <head>
        <style>
            p{{
                font-size:18px;
            }}
            .email-container {{
                font-family: 'Arial', sans-serif;
                color: #333;
                line-height: 1.6;
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                border: 1px solid #ddd;
                border-radius: 10px;
                background-color: #f9f9f9;
            }}
            .email-header {{
                text-align: center;
                padding: 20px;
                background-color: #00aab3;
                color: white;
                border-radius: 10px 10px 0 0;
            }}
            .email-header img {{
                max-width: 100px;
            }}
            .email-body {{
                padding: 20px;
                background-color: white;
                border-radius: 0 0 10px 10px;
            }}
            .email-body p {{
                margin: 10px 0;
            }}
            .button {{
                display: inline-block;
                padding: 10px 20px;
                font-size: 16px;
                color: white;
                background-color: #00aab3;
                text-align: center;
                text-decoration: none;
                border-radius: 5px;
                margin: 20px 0;
            }}
            .email-footer {{
                text-align: center;
                font-size: 12px;
                color: #aaa;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="email-header">
                <h1>Password Reset Request</h1>
                <!-- Optional Logo -->
                <!-- <img src="https://example.com/logo.png" alt="Company Logo"> -->
            </div>
            <div class="email-body">
                <p>Hi {user.firstname} {user.lastname},</p>
                <p>We received a request to reset your password. Click the button below to reset it:</p>
                <p><a class="button" href="{url_for('users.reset_password', token=token, _external=True)}">Reset Password</a></p>
                <p>If you did not request a password reset, please ignore this email or let us know.</p>
                <p>Thanks,<br>The Support Team</p>
            </div>
            <div class="email-footer">
                <p>If you’re having trouble clicking the "Reset Password" button, copy and paste the URL below into your web browser:</p>
                <p><a href="{url_for('users.reset_password', token=token, _external=True)}">{url_for('users.reset_password', token=token, _external=True)}</a></p>
            </div>
        </div>
    </body>
    </html>
    '''
    mail.send(msg)

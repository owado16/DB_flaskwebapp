from flask import render_template
def page_not_found(e):
    return render_template('error.html', error_message='Page not found'), 404

def internal_server_error(e):
    return render_template('error.html', error_message='Internal server error'), 500
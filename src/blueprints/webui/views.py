from flask import current_app, render_template


def index():
    current_app.logger.info('Rendering index page')
    return render_template('index.html', title='Template')

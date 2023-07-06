def render_form_form_css() -> str:
    """
    Render required CSS style tag for form form.
    """
    # Read CSS content from file.
    with open("form/form_form.css", "r") as file:
        css = "<style>"
        css += file.read()
        css += "</style>"
        return css


def render_form_form_js() -> str:
    """
    Render required JS script tag for form form.
    """
    # Read JS content from file.
    with open("form/form_form.js", "r") as file:
        js = "<script>"
        js += file.read()
        js += "</script>"
        return js


def render_form_form_html(form_id: str) -> str:
    """
    Render a form form as HTML.
    """
    form_html = f"""<form action="/forms/{form_id}" method="post" class="form-form">"""

    form_html += """<div class="questions"></div>"""

    form_html += """<div class="add-question"></div>"""

    form_html += "<noscript>"
    form_html += "<p>JavaScript is required to use this form.</p>"
    form_html += "</noscript>"

    form_html += "<hr />"

    form_html += """<label for="question_shuffled">Shuffled:</label>"""
    form_html += (
        """<input type="checkbox" name="question_shuffled" id="question_shuffled" />"""
    )

    form_html += "<br />"

    form_html += """<label for="question_webhook_url">Webhook URL:</label>"""
    form_html += (
        """<input type="url" name="question_webhook_url" id="question_webhook_url" />"""
    )

    form_html += "<br />"

    form_html += """<label for="question_content">Content:</label>"""
    form_html += """<textarea name="question_content" placeholder="This is the Discord message content."></textarea>"""

    form_html += "<br />"

    form_html += """<label for="question_timestamp">Submit at:</label>"""
    form_html += """<input type="datetime-local" name="question_timestamp" id="question_timestamp" />"""

    form_html += "<br />"

    form_html += """<input type="submit" value="Submit" />"""
    form_html += "</form>"
    return form_html

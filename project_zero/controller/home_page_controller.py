def route(app):
    @app.route("/", methods=['GET', 'POST'])
    def hello():
        return "Hello , Welcome to Project Zero [ Banking API ] @ Revature!"

    @app.route("/contact")
    def contact():
        return "Contact Us via Email: donald@email.com or by Phone: 402-555-5555"

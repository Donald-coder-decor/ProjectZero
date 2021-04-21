from controller import user_controller, home_page_controller,account_controller


def route(app):
    # Calls all other other controllers
    user_controller.route(app)
    home_page_controller.route(app)
    account_controller.route(app)

from flask import render_template
from flaskCreate import app

class error:
    
    @app.errorhandler(403)
    def page_not_found(e):
        return render_template("page-error-403.html"),403

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("page-error-404.html"), 404

    @app.errorhandler(500)
    def page_not_found(e):
        return render_template("page-error-500.html"), 500

    @app.errorhandler(503)
    def page_not_found(e):
        return render_template("page-error-503.html"), 503
        
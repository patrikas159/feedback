from flask import render_template
from flask.views import MethodView
from models.feedback import Feedback


class Index(MethodView):
    def get(self):
        feedback = Feedback.query.order_by(Feedback.id.desc()).all()

        return render_template("index.html", feedback=feedback)

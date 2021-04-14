from flask import render_template, session
from flask.views import MethodView
from models.feedback import Feedback


class Index(MethodView):
    def get(self):
        feedback = Feedback.query.order_by(Feedback.id.desc()).all()

        user = session.get('username')

        return render_template("index.html", user=user, feedback=feedback)

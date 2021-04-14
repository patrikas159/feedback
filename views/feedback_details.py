
from models.feedback import Feedback
from flask import redirect, url_for, render_template, session, flash, request
from flask.views import MethodView
from models import db
from models.user import User

class FeedbackDetails(MethodView):


    def get(self, feedback_id):
        feedback = Feedback.query.filter_by(id=feedback_id).first()

        if feedback is None:
            return redirect(url_for('index'))

        feedback.views += 1
        db.session.commit()

        user = User.query.filter_by(id=feedback.id).first()
        return render_template("feedbackDetails.html",
                               feedback=feedback,
                               user=user)


    def post(self, feedback_id):
        feedback = Feedback.query.filter_by(id=feedback_id).first()

        user = User.query.filter_by(username=session.get('username')).first()

        return redirect(url_for('feedback', feedback_id=feedback.id))
from flask import redirect, url_for, render_template
from flask.views import MethodView
from models import db
from models.feedback import Feedback


class FeedbackDetails(MethodView):

    def get(self, feedback_id):
        feedback = Feedback.query.filter_by(id=feedback_id).first()

        if feedback is None:
            return redirect(url_for('index'))

        feedback.views += 1
        db.session.commit()
        return render_template("feedbackDetails.html",
                               feedback=feedback)
        db.session.commit()

        return redirect(url_for('feedback', feedback_id=feedback.id))
from flask import redirect,url_for
from flask.views import MethodView
from forms.feedback_form import FeedbackForm
from models import db
from models.feedback import Feedback




class CreateFeedback(MethodView):

    def post(self):
        feedback_form = FeedbackForm()

        if feedback_form.validate_on_submit():
            new_feedback = Feedback(name=feedback_form.name.data,
                                  category=feedback_form.category.data,
                                  description=feedback_form.description.data)
            db.session.add(new_feedback)
            db.session.commit()

            return redirect(url_for('feedback', feedback_id = Feedback.query.order_by(Feedback.id.desc()).first().id))
        else:
            return redirect(url_for('create_feedback'))
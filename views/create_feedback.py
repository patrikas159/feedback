
from forms.feedback_form import FeedbackForm
from models.feedback import Feedback
from flask import redirect,url_for,render_template, session
from flask.views import MethodView
from models import db
from models.user import User



class CreateFeedback(MethodView):

    def get(self):
        feedback_form = FeedbackForm()

        if session.get('username') is None:
            return redirect(url_for('login'))

        return render_template('createFeedback.html', feedback_form=feedback_form)

    def post(self):
        feedback_form = FeedbackForm()

        if feedback_form.validate_on_submit():
            user = User.query.filter_by(username=session.get('username')).first()
            new_feedback = Feedback(name=feedback_form.name.data,
                                    category=feedback_form.category.data,
                                    ivertinimas=feedback_form.ivertinimas.data,
                                    description=feedback_form.description.data,
                                    kodas=feedback_form.code.data,
                                    user_id=user.id)
            db.session.add(new_feedback)
            db.session.commit()

            return redirect(url_for('feedback', feedback_id = Feedback.query.order_by(Feedback.id.desc()).first().id))
        else:
            return redirect(url_for('create_feedback'))

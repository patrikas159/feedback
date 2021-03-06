from flask import Flask
from flask_socketio import SocketIO, emit
from models.feedback import Feedback
from models import db
from views.feedback_details import FeedbackDetails
from views.index import Index
from views.registration import Register
from views.login import Login
from views.logout import LogOut
from views.create_feedback import CreateFeedback
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
socketio = SocketIO(app=app)

with app.app_context():
    db.create_all(app=app)

app.add_url_rule('/', view_func=Index.as_view('index'))
app.add_url_rule('/register', view_func=Register.as_view('register'))
app.add_url_rule('/login', view_func=Login.as_view('login'))
app.add_url_rule('/logout', view_func=LogOut.as_view('logout'))
app.add_url_rule('/create_feedback', view_func=CreateFeedback.as_view('create_feedback'))
app.add_url_rule('/feedback/<int:feedback_id>', view_func=FeedbackDetails.as_view('feedback'))


@socketio.on('feedback')
def feedback(response):
    feedback_listing = Feedback.query.filter_by(id=response['feedbackId']).first()
    feedback_response = {'feedback_id': feedback_listing.id,
                        'views':feedback_listing.views,}
    emit('feedbackResponse' + str(feedback_response['feedback_id']), feedback_response, broadcast=True)
if __name__ == '__main__':
    socketio.run(app=app, host='localhost')
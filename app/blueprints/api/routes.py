from flask import request,jsonify

from . import bp
from app.models import Post, User
from app.blueprints.api.helpers import token_required

@bp.get('/posts')
@token_required
def api_posts(user):
    result = []
    posts = Post.query.all()
    for post in posts:
        result.append({
            'id':post.id,
            'body':post.body, 
            'timestamp':post.timestamp, 
            'author':post.user_id
            })
    return jsonify(result), 200

#receive posts from single user
@bp.get('/posts/<username>')
@token_required
def user_posts(user,username):
    user = User.query.filter_by(username=username).first() #column and value from url
    if user:
        return jsonify([{
                'id':post.id,
                'body':post.body, 
                'timestamp':post.timestamp, 
                'author':post.user_id
                }for post in user.posts]), 200
    return jsonify([{'message':'Invalid Username'}]), 404

#send single post
@bp.get('/post/<post_id>')
@token_required
def get_post(user, post_id):
    try:
        post = Post.query.get(post_id)
        return jsonify([{
                'id':post.id,
                'body':post.body, 
                'timestamp':post.timestamp, 
                'author':post.user_id
                }])
    except:
        return jsonify([{'message':'Invalid Post ID'}]), 404

#make a post
@bp.post('/post')
@token_required
def make_post(user):
    try:
        content = request.json
        #create a post instance or entry
        post = Post(body=content.get('body'), user_id=user.user_id)
        #commit our post
        post.commit()
        return jsonify([{'message': 'Post Created','body':post.body}])
    except:
        jsonify([{'message': 'invalid form data'}]), 401
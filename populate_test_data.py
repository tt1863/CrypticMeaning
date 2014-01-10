import os
from datetime import datetime

def populate():
    
    add_forum(title="General Forum",
              description="A place to discuss general topics.",
              sequence=1)
    
    add_forum(title="Gaming",
              description="Gaming stuff.",
              sequence=2)
    
    add_forum(title="Web Development",
              description="Web development technologies like Django, ASP.NET, PHP, etc.",
              sequence=3)
    
    add_thread(forum=Forum.objects.get(pk=1),
               title="Woo my first post!",
               date_created=datetime.now(),
               user=User.objects.get(pk=1))
    
    add_thread(forum=Forum.objects.get(pk=1),
               title="The General Forum is here!",
               date_created=datetime.now(),
               user=User.objects.get(pk=1))
    
    add_thread(forum=Forum.objects.get(pk=2),
               title="League of Legends",
               date_created=datetime.now(),
               user=User.objects.get(pk=1))
    
    add_thread(forum=Forum.objects.get(pk=3),
               title="Django",
               date_created=datetime.now(),
               user=User.objects.get(pk=1))
    
    add_post(thread=Thread.objects.get(pk=1),
             content="Why would you post this?",
             date_posted=datetime.now())
    
    add_post(thread=Thread.objects.get(pk=1),
             content="He's an idiot.",
             date_posted=datetime.now())
    
    add_post(thread=Thread.objects.get(pk=2),
             content="This game is pretty cool, anyone want to play?",
             date_posted=datetime.now())
    
    add_post(thread=Thread.objects.get(pk=2),
             content="Sorry, my PC is too slow.",
             date_posted=datetime.now())
    
    add_post(thread=Thread.objects.get(pk=3),
             content="Django is really fun to work with.",
             date_posted=datetime.now())
    
    add_post(thread=Thread.objects.get(pk=3),
             content="I agree.",
             date_posted=datetime.now())
             
    print "Forums added:"
    for f in Forum.objects.all():
        print f
        
    print "Threads added:"
    for t in Thread.objects.all():
        print t
        
    print "Posts added:"
    for p in Post.objects.all():
        print p
        
def add_forum(title, description, sequence):
    f = Forum.objects.get_or_create(title=title, description=description, sequence=sequence)
    return f

def add_thread(forum, title, date_created, user):
    t = Thread.objects.get_or_create(forum=forum, title=title, date_created=date_created, user=user)
    return t

def add_post(thread, content, date_posted):
    p = Post.objects.get_or_create(thread=thread, content=content, date_posted=date_posted)
    return p

# Start execution here!
if __name__ == '__main__':
    print "Starting test data population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CrypticMeaning.settings')
    from forums.models import Forum, Thread, Post
    from django.contrib.auth.models import User
    populate()
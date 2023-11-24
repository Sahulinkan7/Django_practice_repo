from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.db.models.signals import pre_save,post_save
from django.contrib.auth.models import User 
from django.dispatch import receiver

# using decorator receiver

@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    print("+++===========================+++")
    print("logged in successfully ! using decorator ")
    print("sender: ",sender)

@receiver(post_save,sender=User)
def postsave_fun(sender,instance,created,**kwargs):
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    print("sender ",sender)
    print("instance ",instance)
    print("saved user ",instance)
    
@receiver(pre_save,sender=User)
def postsave_fun(sender,instance,**kwargs):
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    print("pre save signal call back function")
    print("sender ",sender)
    print("instance ",instance)
    print("pre saved user ",instance)
# using .connect method 

# def login_success(sender,request,user,**kwargs):
#     print("+++===========================+++")
#     print("logged in successfully ! ")
#     print("sender: ",sender)
    
# user_logged_in.connect(login_success,sender=User)


# def logout_success(sender,request,user,**kwargs):
#     print("+++===========================+++")
#     print("logged out successfully ! ")
#     print("sender: ",sender)
    
# user_logged_out.connect(logout_success,sender=User)
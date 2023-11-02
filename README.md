# Django_practice_repo
A repo for django practice projects

# Project 3
 It covers templates inside project .

# Project 4
 It covers DTL if else conditions , context passing to templates, loops in templates.

# Project 5
 It covers Templates folder of its own inside individual applications to achieve complete isolations from other application or project level templates folders.

# Project 6
 It covers templates inside application and templates at project level as well. templates folder available both in application and project level.
    
# Project 7
 This project is about the static files inside root project directory. static folders consists of css files, javascripts files and images.
  
 To use static files at project level, static folder need to be configured as below in the settings file.

 STATIC_DIR = BASE_DIR / 'static'

 STATICFILES_DIRS = [STATIC_DIR]

# Project 8 

static files inside application. There is no need of any changes in settings.py file for using static files inside applications.

# Project 9

 static files both in project level and application level. need to provide the static folder details inside settings file, for static folder at root directory level.

# Project 10
 
 This project covers the concept of template inheritance in django. 

# Project 11

 This projects covers the concept of template inheritance with static files in django. 

# Project 12 

 This django project includes concept of adding bootstrap files and Hyperlinks in navbars. 

# Resumeproject 
 
 This project covers the concept of template inheritance with static files, adding bootstrap for frontend , etc. A small project to demonstrate the basic web project using django as backend.

# Project 13 
 This projects is about introduction of ORM in django. how to work with django and database using Object Relational Mapper.

 1 ) create model class in applications models.py file
 2 ) python manage.py makemigrations
 3 ) python manage.py migrate

# Project 14
 
 This project is about retrieving data from database and displaying on html page using django orm concept.

# Project 15 

 This project covers the concept of registering models in django admin interface to get access to tables from admin panel.

 models can be registered in two ways.

 1 ) by adding below line of code in admin.py file of application.

        class ModelAdminClassName(admin.ModelAdmin):
                list_display=('fieldname1','fieldname2',....)

        admin.site.register(ModelClassName,ModelAdminClassName)

 2 ) using decorator 

        @admin.register(ModelClassName)
        class ModelAdminClassName(admin.ModelAdmin):
                list_display=('fieldname1','fieldname2',.....)

# Project 16

 This project is about the introduction of FORM API in django.

# Project 17

 This project is about the LOOP concept for retrieving the form fields inside the template.

# Project 18
 This project is about the FORM api fields and form field arguements.
  - > initial
  - > disabled
  - > label
  - > label_suffix
  - > help_text
  - > etc ... 

# Project 19
 This project is about adding css class to form fields through widget arguement in form field.
 
 Example : 
 name=forms.CharField(widget=form.TextInput(attrs={'class':'form-control'}))

# Project 20 
 This project is introduction about form method POST and csrf_token in django form.

# Project 21 
 This project is about getting form data to views and showing the data in terminal and redirecting upon successfull 
 enrollment of user.

# Project 22
 This project is about individual form field validation in forms.py file.

 code as below example : 
  
  def clean_<fieldname>(self):
        <fieldname>=self.cleaned_data['<fieldname>']
        if {condition to check }:
                raise forms.validationerror("message)
        else:
                return <fieldname>

# Project 23 
 This project is about validating the entire form at once using clean method. using clean method dependable fields can be validated at form level. also implemented the custom validator in this project.

 password=forms.CharField(validators=[customvalidatorname],widget=forms.PasswordInput)

# Project 24
 This project is about styling django form validation errors in template using css classes.

# Project 25 
 This project is about inserting form data into database . we have used form api for creating form and through views function creating the model object and saving form data into database.

# Project 26
 This project is about ModelForm. creating forms from models using forms.ModelForm . 

# Project 27 
 Its about practicing dynamic urls. passing arguements in urls dynamically.

# CRUD project1
 This project is about the CRUD operation . ModelForms has been used for form creation and the views are function based.

# Project 28
 This project is about practicing message framework of django. 

# Project 29 
 This project is about practicing usercreation or signup form in django. UserCreationForm forms imported from django.contrib.auth.forms . 
 
# Project 30 
 This project is about customizing the usercreationform. 

# Project 31
 This project is about practicing signup and login features in django webframework. 

# Project 32
 This project is about changing user password.

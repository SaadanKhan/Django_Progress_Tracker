from django.db import models


class User_Role(models.Model):
       role = models.CharField(max_length=50)

       def __str__(self):
              return self.role


class Groups(models.Model):
       name = models.CharField(max_length=50)

       def __str__(self):
              return self.name



class User(models.Model):
       name = models.CharField(max_length=50)
       email = models.EmailField()
       phone = models.CharField(max_length=12)
       password = models.CharField(max_length=500)
       role = models.ForeignKey(User_Role, on_delete=models.CASCADE, null=True)
       group = models.ForeignKey(Groups, on_delete = models.CASCADE, null=True)

       class Meta:
              ordering = ('id',)

       @staticmethod
       def user_name(name):
              try:
                     return User.objects.get(name = name)
              except:
                     return False

       @staticmethod
       def get_email(email):
              try:
                     return User.objects.get(email = email)
              except:
                     return False

       def __str__(self):
              return self.name
       
       def isExist(self):
              if User.objects.filter(email=self.email):
                     return True
              else:
                     return False

       @staticmethod
       def get_grp_by_id(grp_id):
              return User.objects.filter(group = grp_id) 


class Work_update(models.Model):
       name = models.ForeignKey(User, max_length=100, on_delete=models.CASCADE)
       today_work = models.CharField(max_length=500)
       your_course = models.CharField(max_length=500)
       date = models.DateTimeField(auto_now_add=True,blank=True,null=True)

       class Meta:
              ordering = ('id',)
       
       def __str__(self):
              return f"{self.today_work} by {self.name}"

       
       
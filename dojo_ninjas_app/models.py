from django.db import models

class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    desc = models.TextField(default="")
    #ninjas
    def __repr__(self):
        return f"\n\n Name: {self.name}\n City: {self.city}\n State: {self.state}\n ID: ({self.id})"
    def __str__(self):
        return self.name

class Ninjas(models.Model):
    dojo = models.ForeignKey(Dojos, related_name="ninjas", on_delete = models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)

    def __repr__(self):
        return f"\n\n Name: {self.first_name} {self.last_name}\n Dojo: {self.dojo}\n ID: ({self.id})"

dojo4 = Dojos.objects.get(id=4)
dojo5 = Dojos.objects.get(id=5)
dojo6 = Dojos.objects.get(id=6)
dojo7 = Dojos.objects.get(id=7)


ninja1 = Ninjas.objects.get(id =1)
ninja4 = Ninjas.objects.get(id =4)
ninja5 = Ninjas.objects.get(id =5)
ninja6 = Ninjas.objects.get(id =6)
ninja7 = Ninjas.objects.get(id =7)
ninja8 = Ninjas.objects.get(id =8)
ninja9 = Ninjas.objects.get(id =9)
ninja10 = Ninjas.objects.get(id =10)
ninja11 = Ninjas.objects.get(id =11)
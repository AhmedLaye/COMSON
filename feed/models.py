import pandas
from django.db import models

# Create your models here.

class Demandeur(models.Model):
    data=pandas.read_csv('feed\cas_social.csv', index_col=2, skiprows = 2)
    data.sort_values(by = 'Nom')
    nom=models.CharField(max_length=200, null=True)
    prenom=models.CharField(max_length=200, null=True)
    age=models.CharField(max_length=200, null=True)
    tel=models.CharField(max_length=200, null=True)

    def creer(self):
        pandas.DataFrame(self.data)
        print(self.data)
        listeprod={}
        for index, row in self.data.iterrows():
            demandeur=Demandeur.objects.create(
                nom=row.Nom,
                prenom=row.Prénom,
                tel=row.Téléphone
            )
            listeprod[index]=row
            demandeur.save()
        # pandas.DataFrame(listeprod)
        # print(listeprod)
    def __str__(self):
        return f"{self.nom} {self.prenom}"
   
Demandeur.creer(Demandeur)


       


    
    

    
   
    
    
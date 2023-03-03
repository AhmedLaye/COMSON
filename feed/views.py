import base64
import io
import urllib
from urllib import request
from django.shortcuts import render
import pandas
import matplotlib.pyplot as plt
from .models import *

# Create your views here.
def Home(request):
    
    ngorois=Demandeur.objects.all()
    # data=pandas.read_csv('feed\cas_social.csv', index_col=2, skiprows = 2)
    # data.sort_values(by = 'Nom')
    # graph=data.plot()
    # graph.set_xlabel("""Ici on peut mettre ? en foncion de l'age
    # ou le nombre de demande en fonction des demandes
    # """)
    # fig= plt.gcf()
    # buf =io.BytesIO()
    # fig.savefig(buf,format='png')
    # buf.seek(0)
    # string=base64.b64encode(buf.read())
    # uri=urllib.parse.quote(string)
    # plt.show()
    
    # pandas.DataFrame(data)
    # print(data)
    # listeprod={}
    # for index, row in data.iterrows():
    #     produit=Demandeur.objects.create(
    #         nom=row.Nom,
    #         prenom=row.Prénom,
    #         tel=row.Téléphone
    #     )
    #     listeprod[index]=row
    #     produit.save()
    # pandas.DataFrame(listeprod)
    # print(listeprod)

    


    return render(request, 'feed/index.html',{'ngorois':ngorois})


def Modifier(request, myid):
    ngoroi = Demandeur.objects.get(id=myid)
    return render (request, 'feed/detail.html', {'ngoroi':ngoroi})



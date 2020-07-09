from django.shortcuts import render, redirect
from .models import Destination
from .models import Movies
from .models import Ratings
from .models import Trending
from .models import Top
import csv
import pandas as pd
from django.contrib.auth.models import User, auth
import psycopg2
import sys
import dbTable

# Create your views here.
def index(request):

   
    mov = Movies.objects.all()
    
    return render(request,'index.html',{'mov': mov}) 
    #request.session['movie_id'] = mov.movie_id
    


def description(request):
    query = request.GET.get('movid')
    mes = "{}".format(query)
    query1 = request.GET.get('user')
    mes1 = "{}".format(query1)
    movi = Movies.objects.all()
    rat = Ratings.objects.all()
    return render(request,'description.html',{'mes':mes, 'movi':movi, 'mes1':mes1, 'rat':rat})

def vbad(request):
     
     if request.method == 'POST':        
         movie_id= request.POST['movie_id']
         user_id= request.POST['user']
         ratings = '2'
         rat = Ratings(movie_id=movie_id,user_id=user_id,ratings=ratings)
         rat.save()
         
         return redirect('/')





def bad(request):
     
     if request.method == 'POST':        
         movie_id= request.POST['movie_id']
         user_id= request.POST['user']
         ratings = '4'
         rat = Ratings(movie_id=movie_id,user_id=user_id,ratings=ratings)
         rat.save()
         
         return redirect('/')


def mod(request):
     
     if request.method == 'POST':        
         movie_id= request.POST['movie_id']
         user_id= request.POST['user']
         ratings = '6'
         rat = Ratings(movie_id=movie_id,user_id=user_id,ratings=ratings)
         rat.save()
         
         return redirect('/')


def good(request):
     
     if request.method == 'POST':        
         movie_id= request.POST['movie_id']
         user_id= request.POST['user']
         ratings = '8'
         rat = Ratings(movie_id=movie_id,user_id=user_id,ratings=ratings)
         rat.save()
        
         return redirect('/')

def vgood(request):
     
     if request.method == 'POST':        
         movie_id= request.POST['movie_id']
         user_id= request.POST['user']
         ratings = '10'
         rat = Ratings(movie_id=movie_id,user_id=user_id,ratings=ratings)
         rat.save()
         
         return redirect('/')

def recommendation(request):
    mov = Movies.objects.all()
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="1234",
                                  host="127.0.0.1",
                                  database="telusko")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from travello_ratings"
        cursor.execute(postgreSQL_select_Query)
        ratings = cursor.fetchall()
        print("Print each row and it's columns values")
        with open('new.csv','w',newline='') as f:
            thewriter = csv.writer(f)
            thewriter.writerow(['number','movie_id','user_id','ratings'])
            for i in range(len(ratings)): 
                for j in range(1):
                    thewriter.writerow([ratings[i][j],ratings[i][j+1],ratings[i][j+2],ratings[i][j+3]])
        rating = pd.read_csv('new.csv')
        userRatings = rating.pivot_table(index=['user_id'], columns=['movie_id'], values=['ratings'])
        corrMatrix = userRatings.corr()
        query1 = request.GET.get('user')
        mes1 = "{}".format(query1)
        myRatings = userRatings.loc[mes1].dropna()
        simCandidates = pd.Series()
        for i in range(0, len(myRatings.index)):
            print (myRatings.index[i])
            sims = corrMatrix[myRatings.index[i]].dropna()
            sims = sims.map(lambda x: x * myRatings[i])
            simCandidates = simCandidates.append(sims)
        
        print ("sorting...")
        simCandidates.sort_values(inplace = True, ascending = False )
        print (simCandidates.head(20))
        
            
            
        simCandidates = simCandidates.groupby(simCandidates.index).sum()
        simCandidates.sort_values(inplace = True, ascending = False )    
        print(simCandidates.head(20))
        
            
        filteredsim = simCandidates.drop(myRatings.index)
        print(filteredsim.head(20))
        remov = []
        
        for i in range(0, len(filteredsim)):
            remov.append(filteredsim.index[i][1])
            
        
        
    

    except (Exception, psycopg2.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)
    return render(request,'recommendation.html')
     
def trending(request):
    query1 = request.GET.get('user')
    mes1 = "{}".format(query1)
    tren = Trending.objects.all()
    return render(request,'trending.html',{'mes1':mes1,'tren':tren})


def descriptiont(request):
    query = request.GET.get('movid')
    mes = "{}".format(query)
    query1 = request.GET.get('user')
    mes1 = "{}".format(query1)
    
    rat = Ratings.objects.all()
    tren = Trending.objects.all()
    return render(request,'descriptiont.html',{'mes':mes,  'mes1':mes1, 'rat':rat,'tren':tren})

def top(request):
    query1 = request.GET.get('user')
    mes1 = "{}".format(query1)
    top = Top.objects.all()
    return render(request,'top.html',{'mes1':mes1,'top':top})


def descriptionto(request):
    query = request.GET.get('movid')
    mes = "{}".format(query)
    query1 = request.GET.get('user')
    mes1 = "{}".format(query1)
    
    rat = Ratings.objects.all()
    top = Top.objects.all()
    return render(request,'descriptionto.html',{'mes':mes,  'mes1':mes1, 'rat':rat,'top':top})
import base64
import io
from bs4 import BeautifulSoup
from django.shortcuts import render
from datetime import datetime
from matplotlib import pyplot as plt
import requests
from wordcloud import WordCloud

# home/views.py

def home(request):
    return render(request, 'home/index.html')

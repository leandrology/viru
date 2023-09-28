from django.shortcuts import render, redirect
from django.contrib import messages
import subprocess


# Create your views here.

def train(request):
    if request.method == 'POST':
        # Execute the script to restart the Rasa server
        action = request.POST.get('action')
        if action == 'train':
            subprocess.run(["rasa", "train"], cwd="C:\\Users\\Leander\\Desktop\\dev\\ruby\\AI-BI\\", shell=False)
            # subprocess.run(["rasa", "train"], cwd="C:\\Users\\Philip\\Documents\\ServingIntel\\AI-BI", shell=True)
            # subprocess.run(["echo","1969Firebird!", "|","sudo", "-S","systemctl", "restart", "rasa.service"], cwd="/home/lancewbell/AI-BI/")
            # subprocess.run(["echo","1969Firebird!", "|","sudo", "-S","systemctl", "restart", "rasa-actions.service"], cwd="/home/lancewbell/AI-BI/")
    return redirect(request.META.get('HTTP_REFERER',''))


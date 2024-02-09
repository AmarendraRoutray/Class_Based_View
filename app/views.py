from django.shortcuts import render

# Create your views here.
from .forms import *
from django.http import HttpResponse
from django.views.generic import View,TemplateView,FormView


# function based view

def addSong_fbv(request):
    ESF = SongsForm()
    if request.method == 'POST':
        SFDO = SongsForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Song added by FBV')

    return render(request,'addSong_fbv.html',{'ESF':ESF})


# class based view

class addSong_cbv(View):
    def get(self,request):
        ESF = SongsForm()
        return render(request,'addSong_cbv.html',{'ESF':ESF})
    
    def post(self,request):
        SFDO = SongsForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Song added by CBV')



# Template-View
      
class TemplateHtml(TemplateView):
    template_name='templateView.html'
    
    def get_context_data(self,**kwargs):
        ECDO = super().get_context_data(**kwargs)
        ECDO['form'] = WhiskyForm
        return ECDO
    
    def post(self,request):
        WDO = WhiskyForm(request.POST)
        if WDO.is_valid():
            WDO.save()
            return HttpResponse("Let's party..party...''Template_view''..")
    

class insertWhisky(FormView):
    template_name='templateView.html'
    form_class = WhiskyForm
    
    def form_valid(self,form):
        form.save()
        return HttpResponse("Let's party..party...''Form_view''..")
    
    
    

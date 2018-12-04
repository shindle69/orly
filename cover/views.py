from django.conf import settings
from django.shortcuts import render,redirect
from .forms import CoverForm
from PIL import Image,ImageDraw,ImageFont
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method =='POST':
        form=CoverForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            
    else:
        form=CoverForm()
    return render(request,'cover/index.html',{
        'form':form,
    })

def image_generator(request):
    title = request.GET['title']
    top_text = request.GET['top_text']
    author = request.GET['author']
    animal_code = request.GET['animal_code']
    color_code = request.GET['color_code']
    guide_text = request.GET['guide_text']
    guide_text_placement = request.GET['guide_text_placement']

    im=Image.new('RGB',(256,256),'white')

    ttf_path=settings.ROOT('assets','fonts','NanumBarunGothicBold.ttf')
    # get a font    
    d = ImageDraw.Draw(im)    

    fnt = ImageFont.truetype(ttf_path, 40)
    d.text((10,10), title , font=fnt, fill=(0,255,0,128))  

    fnt = ImageFont.truetype(ttf_path, 30)
    d.text((10,60), top_text , font=fnt, fill=(0,255,0,255))

    fnt = ImageFont.truetype(ttf_path, 20)
    d.text((10,110), author , font=fnt, fill=(0,255,0,255))

    response=HttpResponse(content_type='image/png')
    im.save(response,format='PNG')
    return response
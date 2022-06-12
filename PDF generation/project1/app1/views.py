from django.shortcuts import render

from .forms import LaptopForm
from .models import Laptop
from fpdf import FPDF
from django.http import FileResponse

# Create your views here.
def AddLaptopView(request):
    template_name='app1/addlaptop.html'
    form = LaptopForm()
    if request.method=='POST':
        form=LaptopForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,template_name,context)

def ShowLaptopView(request):
    data=Laptop.objects.all()
    template_name='app1/showlaptop.html'
    context={'obj':data}
    return render(request,template_name,context)

def ReportView(request,id):
    data=Laptop.objects.get(id=id)
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('courier', 'B', 16)
    pdf.cell(40, 10, f'This is record of  laptop id: {data.lid}',0,1)
    pdf.cell(40, 10, '',0,1)
    pdf.set_font('courier', '', 12)
    
    
    LID=data.lid
    NAME=data.name
    BRAND=data.brand
    RAM=data.ram
    ROM=data.rom
    HDD=data.hdd
    SSD=data.ssd
    PRICE=data.price
    li=[LID,NAME,BRAND,RAM,ROM,HDD,SSD,PRICE]
    #pdf.cell(200, 8, f"{'Item'.ljust(30)} {'Amount'.rjust(20)}", 0, 1)
    #pdf.line(10, 30, 150, 30)
    #pdf.line(10, 38, 150, 38)
    pdf.cell(200, 8, f"LAPTOP ID:{li[0]}", 0, 1)
    pdf.cell(200, 8, f"NAME:{li[1]}", 0, 1)
    pdf.cell(200, 8, f"BRAND:{li[2]}", 0, 1)
    pdf.cell(200, 8, f"RAM:{li[3]}", 0, 1)
    pdf.cell(200, 8, f"ROM:{li[4]}", 0, 1)
    pdf.cell(200, 8, f"HDD:{li[5]}", 0, 1)
    pdf.cell(200, 8, f"SSD:{li[6]}", 0, 1)
    pdf.cell(200, 8, f"PRICE:{li[7]}", 0, 1)

    pdf.output(f'{NAME}.pdf', 'F')

    return FileResponse(open(f'{NAME}.pdf',"rb"),as_attachment=True,content_type='application/pdf')


def AllReportView(request):
    data=Laptop.objects.all()
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('courier', 'B', 16)
    pdf.cell(40, 10, 'This is what you have sold this month so far:',0,1)
    pdf.cell(40, 10, '',0,1)
    pdf.set_font('courier', '', 12)
    li=[]
    for i in data:
        LID=i.lid
        NAME=i.name
        BRAND=i.brand
        RAM=i.ram
        ROM=i.rom
        HDD=i.hdd
        SSD=i.ssd
        PRICE=i.price
        li.append(LID)
        li.append(NAME)
        li.append(BRAND)
        li.append(RAM)
        li.append(ROM)
        li.append(HDD)
        li.append(SSD)
        li.append(PRICE)
    #pdf.cell(200, 8, f"{'Item'.ljust(30)} {'Amount'.rjust(20)}", 0, 1)
    #pdf.line(10, 30, 150, 30)
    #pdf.line(10, 38, 150, 38)
    for line in li:
        pdf.cell(200, 8, f"{line}", 0, 1)

    pdf.output('Laptop.pdf', 'F')

    return FileResponse(open('Laptop.pdf',"rb"),as_attachment=True,content_type='application/pdf')
    
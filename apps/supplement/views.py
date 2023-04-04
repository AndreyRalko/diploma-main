from django.shortcuts import render
from .models import Faculties,Cafedras,Groups,Common_Info,Student_Info
from django.db import connection



def index(request):

    if 'facultyID' not in request.POST:
        sel_FacultyID=2
        sel_CafedraID=2
    else:
        sel_FacultyID=int(request.POST['facultyID'])
        if 'facultyID' not in request.POST:
            sel_CafedraID=2
        else:
            sel_CafedraID=int(request.POST['cafedraID'])

    

    sql="SELECT g.name,g.groupID from groups g ,specializations s,profession_cafedra pc,students s1,studyforms s2 WHERE g.specializationID=s.id AND s.prof_caf_id=pc.id AND pc.cafedraID="+str(sel_CafedraID)+" and g.groupID=s1.GroupID AND s1.isStudent=1  AND s1.StudyFormID=s2.Id AND s1.CourseNumber=s2.courseCount GROUP BY g.groupID"
    
    context = {
        'Faculties': Faculties.objects.using("platonus").filter(FacultyID__in=[2,4,8,11]),
        'sel_FacultyID': sel_FacultyID,
        'cafedras':  Cafedras.objects.using("platonus").filter(FacultyID=sel_FacultyID).filter(cafedraID__in=[2,4,6,8,10,12,15,16,17,19,20,21,22,26,28,29,44,45,47]),
        'groups': Groups.objects.using("platonus").raw(sql)
    }
   
    return render(request, 'supplement_create.html',context)

def group_index(request):

    sql_common_info="SELECT g.groupID,g.name,s.id as specializationID,s.nameru,s.namekz,s.nameen,s.specializationCode FROM groups g,specializations s WHERE g.groupID="+request.POST['groupID']+" AND g.specializationID=s.id"
    sql_Student_Info="SELECT StudentID,lastname,firstname,patronymic,lastname_en,firstname_en,BirthDate,seriyaAttestata,nomerAttestata,dataVydachiAttestata,enterexamsen,StartDate from students WHERE isStudent=1 AND isinretire<>1 AND groupID="+request.POST['groupID']

    context = {
        'common_info': Common_Info.objects.using("platonus").raw(sql_common_info),
        'Student_Info':Student_Info.objects.using("platonus").raw(sql_Student_Info)
    }
    return render(request, 'group.html',context)


    


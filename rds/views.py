import MySQLdb.connections

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import csrf

conn = MySQLdb.connect(host='localhost', user='root', passwd='root', db='rds')
cursor = conn.cursor()


# Create your views here.
def hello(request):
    return render(request, 'hello.html')


def details(request):
    stmt = 'select * from students'
    cursor.execute(stmt)
    # assert isinstance(cursor, object)
    data = cursor.fetchall();
    records = []
    for d in data:
        records.append({'id': d[1], 'name': d[0]})
    args = {'records': records}
    return render(request, 'details.html', args)


def new_rec(request):
    return render(request, 'new_rec.html')


def insert(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = request.POST
        name = form.get('name')
        id = form.get('id')
        print name, id
        stmt='insert into students values("%s",%d)'%(name, int(id))
        print stmt
        cursor.execute(stmt)
        cursor.execute('commit')
    return HttpResponseRedirect('/')

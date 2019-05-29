import requests

BASE_URL='https://glacial-anchorage-13641.herokuapp.com/'
ENDPOINT='emp/'


def get_emp_data():
    oo=input('order by "emp_no" or "emp_sal" or "emp_name"')
    li=input('enter limit')
    orr=input('input asc or desc')
    
    resp=requests.get(BASE_URL+ENDPOINT+'orderby={}&limit={}&ordering={}'.format(oo,li,orr))
    print(resp.json())

    

get_emp_data()

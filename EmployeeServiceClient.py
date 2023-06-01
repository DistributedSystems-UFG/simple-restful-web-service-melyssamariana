import requests
import const


def updateSalary(id,new_salary):
    api_base_url = 'http://' + const.IP_ADD + ':' + str(const.PORT) + '/empdb/employee'
    api_url = api_base_url + '/' + str(id)
    update = {'salary':new_salary}
    response = requests.put(api_url, json=update)
    print (response.json())

def checkID(id):
    api_base_url = 'http://' + const.IP_ADD + ':' + str(const.PORT) + '/empdb/employee'
    api_url = api_base_url + '/' + str(id)
    response = requests.get(api_url)
    print("TESTE")
    print(response.json())
    if response.json() == []:
        return False
    else:
        return True

def averageSalaryAll():
    api_base_url = 'http://' + const.IP_ADD + ':' + str(const.PORT) + '/empdb/employee'
    response = requests.get(api_base_url)
    sum = 0
    for i in response.json()['emps']:
        sum += i['salary']
    return sum/len(response.json()['emps'])

def serviceTester():
    api_base_url = 'http://' + const.IP_ADD + ':' + str(const.PORT) + '/empdb/employee'
    #print('Average salary of all employees: ' + str(averageSalaryAll()))
    print('Employee with ID 101 exists: ' + str(checkID(101)))
    print('Employee with ID 999 exists: ' + str(checkID(999)))
    print('Updating salary of employee with ID 101 to 100000')
    updateSalary(101, 100000)
'''
    # Test get_all_employees endpoint
    api_url = api_base_url 
    response = requests.get(api_url)
    print (response.json())

    # Test get_an_employee endpoint
    api_url = api_base_url + '/201'
    response = requests.get(api_url)
    print (response.json())

    # Test update_employee endpoint
    api_url = api_base_url + '/101'
    update = {"title":"Programmer"}
    response = requests.put(api_url, json=update)
    print (response.json())

    # Test create_employee endpoint
    api_url = api_base_url
    employee = {"id":"301", "name":"J. Silva", "title":"Senior Programmer"}
    response = requests.post(api_url, json=employee)
    print (response.json())

    # Test delete_employee endpoint
    api_url = api_base_url + '/101'
    response = requests.delete(api_url)
    print (response.json())
'''
if __name__ == '__main__':
    serviceTester()
